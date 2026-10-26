#!/usr/bin/env python3
"""Running efficiency at equal HR from steady, flat 2-min windows. Usage:
  efficiency.py --after YYYY-MM-DD   all runs since date
  efficiency.py <activity_id> [...]  specific runs

pace@147 = GAP pace at HR 147 from windows with HR 140-155 (method in 03_training_log.md).
'early' uses only minutes 10-45, so long runs compare with easy runs without drift.
Compare only rows with comparable=True: >=48 h after legs, no "maska" in the run name.
"""
import csv
import json
import statistics as st
import sys
import urllib.parse
import urllib.request
from datetime import datetime, timedelta
from pathlib import Path

from metrics import minetti, pace
from strava import get

HUB = Path(__file__).resolve().parent.parent / "fitness-hub"
HR_REF, HR_LO, HR_HI = 147, 140, 155
LEGS_GAP_H = 48


def windows(s, tmax=None):
    t, v, mv = s["time"]["data"], s["velocity_smooth"]["data"], s["moving"]["data"]
    gr = s.get("grade_smooth", {}).get("data") or [0] * len(t)
    hr = s["heartrate"]["data"]
    n, out, i0 = len(t), [], 0
    steep = [t[k] for k in range(n) if gr[k] > 8]
    for t0 in range(600, int(t[-1]) - 120, 60):
        if tmax and t0 + 120 > tmax:
            break
        while i0 < n and t[i0] < t0:
            i0 += 1
        idx = [k for k in range(i0, n) if t[k] < t0 + 120]
        if len(idx) < 90:
            continue
        sp = [v[k] for k in idx]
        # running steadily, not stopped or walking
        if sum(1 for k in idx if mv[k] and v[k] > 1.5) < 0.95 * len(idx) or st.mean(sp) < 2.0:
            continue
        # flat enough that GAP is trustworthy
        g = sorted(abs(gr[k]) for k in idx)
        if g[int(0.9 * len(g))] > 6 or abs(st.mean(gr[k] for k in idx)) > 3:
            continue
        h = [hr[k] for k in idx]
        if max(h) - min(h) > 10 or max(sp) > 1.4 * st.mean(sp):  # HR steady, no strides
            continue
        if any(t0 - 300 <= x < t0 for x in steep):  # HR still recovering from a steep hill
            continue
        gap = st.mean(v[k] * minetti(gr[k] / 100) / 3.6 for k in idx)
        out.append((st.mean(h), gap))
    return out


def at_ref_hr(w):
    w = [x for x in w if HR_LO <= x[0] <= HR_HI]
    if not w:
        return None, 0
    return pace(st.median(g / h for h, g in w) * HR_REF), len(w)


def leg_sessions():
    with open(HUB / "gym_sets.csv") as f:
        legs = {r["workout_id"] for r in csv.DictReader(f) if r["muscle_group"] == "legs"}
    with open(HUB / "gym_workouts.csv") as f:
        return sorted(datetime.fromisoformat(r["end_local"] or r["start_local"])
                      for r in csv.DictReader(f) if r["workout_id"] in legs)


def temperature(latlng, start, minutes):
    if not latlng:
        return None
    lat, lon = (round(x, 1) for x in latlng)  # ~10 km, the exact route never leaves the machine
    day = start.date().isoformat()
    hours = {(start + timedelta(minutes=m)).strftime("%Y-%m-%dT%H:00") for m in range(0, minutes + 1, 15)}
    # archive (ERA5) lags ~5 days, the forecast API covers recent days
    for url in ("https://archive-api.open-meteo.com/v1/archive", "https://api.open-meteo.com/v1/forecast"):
        q = urllib.parse.urlencode({"latitude": lat, "longitude": lon, "hourly": "temperature_2m",
                                    "start_date": day, "end_date": day, "timezone": "auto"})
        try:
            with urllib.request.urlopen(f"{url}?{q}", timeout=20) as r:
                h = json.load(r)["hourly"]
        except Exception:
            continue
        vals = [x for k, x in zip(h["time"], h["temperature_2m"]) if k in hours and x is not None]
        if vals:
            return round(st.mean(vals), 1)
    return None


def analyze(act_id, legs):
    a = get(f"/activities/{act_id}")
    start = datetime.fromisoformat(a["start_date_local"][:19])  # local time despite the "Z"
    before = [x for x in legs if x < start]
    since = round((start - before[-1]).total_seconds() / 3600) if before else None
    mask = "maska" in a["name"].lower()
    out = {"date": start.date().isoformat(), "name": a["name"], "km": round(a["distance"] / 1000, 2),
           "temp_c": temperature(a.get("start_latlng"), start, round(a["elapsed_time"] / 60)),
           "h_since_legs": since, "mask": mask}
    s = get(f"/activities/{act_id}/streams",
            keys="time,heartrate,velocity_smooth,moving,grade_smooth", key_by_type="true")
    if "heartrate" not in s:
        return out
    out["pace@147_early"], out["n_early"] = at_ref_hr(windows(s, tmax=45 * 60))
    out["pace@147"], out["n"] = at_ref_hr(windows(s))
    out["comparable"] = (since is None or since >= LEGS_GAP_H) and not mask and out["n_early"] >= 4
    return out


if __name__ == "__main__":
    args = sys.argv[1:]
    if not args:
        sys.exit(__doc__)
    if args[0] == "--after":
        ts = int(datetime.strptime(args[1], "%Y-%m-%d").timestamp())
        ids = [x["id"] for x in sorted(get("/athlete/activities", after=ts, per_page=100),
                                       key=lambda x: x["start_date_local"]) if x["sport_type"] == "Run"]
    else:
        ids = args
    legs = leg_sessions()
    for i in ids:
        print(analyze(i, legs))
