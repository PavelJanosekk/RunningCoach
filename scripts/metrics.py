#!/usr/bin/env python3
"""Per-run metrics from Strava per-second streams. Usage:
  metrics.py --after YYYY-MM-DD      all runs since date
  metrics.py <activity_id> [...]     specific runs
"""
import sys
from datetime import datetime

from strava import get

LTHR = 172


def minetti(g):
    g = max(-0.30, min(0.30, g))
    return 155.4*g**5 - 30.4*g**4 - 43.3*g**3 + 46.3*g**2 + 19.5*g + 3.6


def pace(v):
    if not v or v <= 0.3:
        return "-"
    s = 1000 / v
    return f"{int(s // 60)}:{int(round(s % 60)):02d}"


def wmean(idx, arr, dts):
    w = sum(dts[i] for i in idx)
    return sum(arr[i] * dts[i] for i in idx) / w if w else 0


def analyze(act_id):
    a = get(f"/activities/{act_id}")
    s = get(f"/activities/{act_id}/streams",
            keys="time,distance,heartrate,velocity_smooth,moving,grade_smooth", key_by_type="true")
    t, d = s["time"]["data"], s["distance"]["data"]
    v, mv = s["velocity_smooth"]["data"], s["moving"]["data"]
    gr = s.get("grade_smooth", {}).get("data") or [0] * len(t)
    hr = s.get("heartrate", {}).get("data")
    n = len(t)
    gap = [v[i] * minetti(gr[i] / 100) / 3.6 for i in range(n)]
    dts = [min(10, t[i + 1] - t[i]) for i in range(n - 1)] + [1]
    moving = [i for i in range(n) if mv[i] and v[i] > 1.0]
    out = {"date": a["start_date_local"][:10], "name": a["name"], "km": round(a["distance"] / 1000, 2),
           "pace": pace(wmean(moving, v, dts)), "gap": pace(wmean(moving, gap, dts)),
           "rpe": a.get("perceived_exertion")}
    first10 = [i for i in moving if t[i] < 600]
    out["pace_first10min"] = pace(wmean(first10, v, dts))
    if hr:
        tot = sum(dts[i] for i in moving) or 1
        for thr in (153, 157, 162):
            out[f"pct>{thr}"] = round(100 * sum(dts[i] for i in moving if hr[i] > thr) / tot)
        ss = [i for i in moving if t[i] >= 600]
        if len(ss) > 120:
            out["hr_ss"] = round(wmean(ss, hr, dts))
            out["EF_gap"] = round(wmean(ss, gap, dts) * 60 / wmean(ss, hr, dts), 3)
            half, acc, h1, h2 = sum(dts[i] for i in ss) / 2, 0, [], []
            for i in ss:
                (h1 if acc < half else h2).append(i)
                acc += dts[i]
            r1 = wmean(h1, gap, dts) / wmean(h1, hr, dts)
            r2 = wmean(h2, gap, dts) / wmean(h2, hr, dts)
            # decoupling is only meaningful for steady runs >= ~50 min
            out["decoupling_gap_pct"] = round(100 * (r1 - r2) / r1, 1)
            band = [i for i in ss if 143 <= hr[i] <= 150]
            if sum(dts[i] for i in band) >= 300:
                out["gap@hr143-150"] = pace(wmean(band, gap, dts))
            out["min_163-172"] = round(sum(dts[i] for i in moving if 163 <= hr[i] <= LTHR) / 60, 1)
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
    for i in ids:
        print(analyze(i))
