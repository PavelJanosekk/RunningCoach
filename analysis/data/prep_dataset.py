import json, sys, time, math, urllib.request, urllib.parse, collections
from pathlib import Path
from datetime import datetime, timedelta

sys.path.insert(0, "/Users/pavel.janosek/personal/RunningCoach/scripts")
import strava

OUT = Path("/private/tmp/claude-502/-Users-pavel-janosek-personal-RunningCoach/0d5cf212-6afa-4de1-84af-ed4e781cfb85/scratchpad/dataset")
RAW = OUT / "streams"
RAW.mkdir(parents=True, exist_ok=True)
LIST = Path(OUT.parent / "all_list.jsonl")
LTHR = 172


def api(path, **params):
    url = strava.API + path + ("?" + urllib.parse.urlencode(params) if params else "")
    req = urllib.request.Request(url, headers={"Authorization": "Bearer " + strava.access_token()})
    with urllib.request.urlopen(req) as r:
        usage = int(r.headers.get("x-readratelimit-usage", "0,0").split(",")[0])
        data = json.load(r)
    if usage >= 92:
        wait = 900 - (time.time() % 900) + 5
        print(f"rate limit {usage}, sleeping {int(wait)}s", flush=True)
        time.sleep(wait)
    return data


def zone(h):
    if h <= 137: return "Z1"
    if h <= 153: return "Z2"
    if h <= 162: return "Z3"
    if h <= 172: return "Z4"
    return "Z5"


def minetti(g):
    g = max(-0.30, min(0.30, g))
    return 155.4*g**5 - 30.4*g**4 - 43.3*g**3 + 46.3*g**2 + 19.5*g + 3.6


def fmt_pace(v):
    if not v or v <= 0.3: return None
    s = 1000 / v
    return f"{int(s//60)}:{int(round(s%60)):02d}"


rows = [json.loads(l) for l in LIST.read_text().splitlines()]
runs = [r for r in rows if r["type"] == "Run"]
others = [r for r in rows if r["type"] != "Run"]

# fetch streams
for r in runs:
    f = RAW / f"{r['id']}.json"
    if f.exists():
        continue
    try:
        s = api(f"/activities/{r['id']}/streams",
                keys="time,distance,heartrate,altitude,velocity_smooth,cadence,moving,grade_smooth",
                key_by_type="true")
    except Exception as e:
        s = {"error": str(e)}
    f.write_text(json.dumps(s))
    print("stream", r["id"], r["date"][:10], flush=True)

# lap details for structured workouts
WORKOUTS = {19971567878: "LTHR test", 20083421075: "Threshold #1", 20223619746: "Threshold #2", 20291838853: "Easy + strides"}
laps_out = {}
for wid, label in WORKOUTS.items():
    f = RAW / f"detail_{wid}.json"
    if not f.exists():
        f.write_text(json.dumps(api(f"/activities/{wid}")))
    d = json.loads(f.read_text())
    laps_out[label] = {"id": wid, "date": d["start_date_local"], "laps": [{
        "lap": l["lap_index"], "dist_m": round(l["distance"]), "moving_s": l["moving_time"],
        "pace": fmt_pace(l.get("average_speed")), "hr_avg": l.get("average_heartrate"),
        "hr_max": l.get("max_heartrate"), "cadence_spm": round(2*l["average_cadence"]) if l.get("average_cadence") else None,
        "elev_gain": l.get("total_elevation_gain")} for l in d.get("laps", [])]}


def analyze(r, s):
    out = {k: r[k] for k in ("id", "date", "name", "km", "moving", "elapsed", "pace", "hr_avg", "hr_max", "elev")}
    dt0 = datetime.fromisoformat(r["date"].replace("Z", ""))
    out["weekday"] = dt0.strftime("%a")
    out["start_hour"] = dt0.hour
    if "error" in s or "time" not in s:
        out["stream_error"] = s.get("error", "no streams")
        return out, []
    t = s["time"]["data"]; d = s["distance"]["data"]
    v = s.get("velocity_smooth", {}).get("data")
    hr = s.get("heartrate", {}).get("data")
    alt = s.get("altitude", {}).get("data")
    cad = s.get("cadence", {}).get("data")
    mov = s.get("moving", {}).get("data") or [True]*len(t)
    gr = s.get("grade_smooth", {}).get("data") or [0]*len(t)
    n = len(t)
    if v is None:
        v = [0]+[(d[i]-d[i-1])/max(1, t[i]-t[i-1]) for i in range(1, n)]
    gap = [v[i]*minetti(gr[i]/100)/3.6 for i in range(n)]
    dts = [min(10, t[i+1]-t[i]) for i in range(n-1)] + [1]
    movmask = [mov[i] and v[i] > 1.0 for i in range(n)]
    out["has_hr"] = hr is not None
    # cadence
    cads = [cad[i] for i in range(n) if cad and movmask[i] and cad[i] > 60]
    out["cadence_spm"] = round(2*sum(cads)/len(cads)) if cads else None
    # GAP overall
    mt = sum(dts[i] for i in range(n) if movmask[i])
    out["gap_pace"] = fmt_pace(sum(gap[i]*dts[i] for i in range(n) if movmask[i]) / mt) if mt else None
    splits = []
    if hr:
        zt = collections.Counter()
        for i in range(n):
            if movmask[i]:
                zt[zone(hr[i])] += dts[i]
        tot = sum(zt.values()) or 1
        out["zone_min"] = {z: round(zt[z]/60, 1) for z in ("Z1", "Z2", "Z3", "Z4", "Z5")}
        out["zone_pct"] = {z: round(100*zt[z]/tot, 1) for z in ("Z1", "Z2", "Z3", "Z4", "Z5")}
        out["min_above_153"] = round((zt["Z3"]+zt["Z4"]+zt["Z5"])/60, 1)
        # steady-state window: after 10 min moving
        idx = [i for i in range(n) if movmask[i] and t[i] >= 600]
        if len(idx) > 120:
            w = [dts[i] for i in idx]; W = sum(w)
            mhr = sum(hr[i]*dts[i] for i in idx)/W
            mv = sum(v[i]*dts[i] for i in idx)/W
            mg = sum(gap[i]*dts[i] for i in idx)/W
            out["ss_hr"] = round(mhr, 1)
            out["EF_raw"] = round(mv*60/mhr, 3)   # m/min per bpm
            out["EF_gap"] = round(mg*60/mhr, 3)
            half = W/2; acc = 0; h1 = []; h2 = []
            for i in idx:
                (h1 if acc < half else h2).append(i); acc += dts[i]
            def ratio(ix, arr):
                ww = sum(dts[i] for i in ix)
                return (sum(arr[i]*dts[i] for i in ix)/ww) / (sum(hr[i]*dts[i] for i in ix)/ww)
            out["decoupling_raw_pct"] = round(100*(ratio(h1, v)-ratio(h2, v))/ratio(h1, v), 1)
            out["decoupling_gap_pct"] = round(100*(ratio(h1, gap)-ratio(h2, gap))/ratio(h1, gap), 1)
            out["hr_half1"] = round(sum(hr[i]*dts[i] for i in h1)/sum(dts[i] for i in h1), 1)
            out["hr_half2"] = round(sum(hr[i]*dts[i] for i in h2)/sum(dts[i] for i in h2), 1)
            # HR at standardized GAP pace 5:50-6:10/km
            band = [i for i in idx if 2.70 <= gap[i] <= 2.86]
            bt = sum(dts[i] for i in band)
            if bt >= 300:
                out["hr_at_gap_6min_km"] = round(sum(hr[i]*dts[i] for i in band)/bt, 1)
                out["hr_at_gap_6min_km_minutes"] = round(bt/60, 1)
            # GAP pace at HR 143-150
            band2 = [i for i in idx if 143 <= hr[i] <= 150]
            bt2 = sum(dts[i] for i in band2)
            if bt2 >= 300:
                out["gap_pace_at_hr_143_150"] = fmt_pace(sum(gap[i]*dts[i] for i in band2)/bt2)
                out["gap_pace_at_hr_143_150_minutes"] = round(bt2/60, 1)
        # first 3 km vs rest
        f3 = [i for i in range(n) if movmask[i] and d[i] <= 3000]
        rest = [i for i in range(n) if movmask[i] and d[i] > 3000]
        if f3 and rest and d[-1] > 4500:
            def seg(ix):
                ww = sum(dts[i] for i in ix)
                return {"pace": fmt_pace(sum(v[i]*dts[i] for i in ix)/ww),
                        "gap": fmt_pace(sum(gap[i]*dts[i] for i in ix)/ww),
                        "hr": round(sum(hr[i]*dts[i] for i in ix)/ww, 1),
                        "min_above_153": round(sum(dts[i] for i in ix if hr[i] > 153)/60, 1),
                        "elev_net_m": round(alt[ix[-1]]-alt[ix[0]]) if alt else None}
            out["first3km"] = seg(f3); out["after3km"] = seg(rest)
        # HR quality
        early = [hr[i] for i in range(n) if 120 <= t[i] <= 300 and v[i] > 2.2]
        out["hr_dropout_early"] = bool(early) and (sum(1 for h in early if h < 110)/len(early) > 0.3)
        spikes = sum(1 for i in range(5, n) if abs(hr[i]-hr[i-5]) > 20 and t[i]-t[i-5] <= 6)
        out["hr_spike_count"] = spikes
        srt = sorted(hr); out["hr_p99"] = srt[int(0.99*(len(srt)-1))]
    # km splits
    k = 1; start = 0
    for i in range(n):
        if d[i] >= 1000*k or i == n-1:
            ix = [j for j in range(start, i+1) if movmask[j]] or list(range(start, i+1))
            ww = sum(dts[j] for j in ix) or 1
            sp = {"km": k, "dist_m": round(d[i]-(1000*(k-1))),
                  "pace": fmt_pace(sum(v[j]*dts[j] for j in ix)/ww),
                  "gap": fmt_pace(sum(gap[j]*dts[j] for j in ix)/ww),
                  "elev_diff": round(alt[i]-alt[start], 1) if alt else None}
            if hr:
                sp["hr"] = round(sum(hr[j]*dts[j] for j in ix)/ww, 1)
                sp["hr_max"] = max(hr[j] for j in ix)
            splits.append(sp); start = i; k += 1
    return out, splits


summ, splits_all = [], {}
for r in runs:
    s = json.loads((RAW / f"{r['id']}.json").read_text())
    o, sp = analyze(r, s)
    summ.append(o); splits_all[str(r["id"])] = {"date": r["date"], "name": r["name"], "splits": sp}

# duplicates (same day, same km)
seen = {}
for o in summ:
    key = (o["date"][:10], round(o["km"], 1))
    if key in seen:
        o["duplicate_of"] = seen[key]
    else:
        seen[key] = o["id"]

# weekly
def monday(ds):
    dd = datetime.fromisoformat(ds.replace("Z", "")).date()
    return (dd - timedelta(days=dd.weekday())).isoformat()

weeks = collections.OrderedDict()
first = datetime.fromisoformat(runs[0]["date"].replace("Z", "")).date()
last = datetime.fromisoformat(rows[-1]["date"].replace("Z", "")).date()
m = first - timedelta(days=first.weekday())
while m <= last:
    weeks[m.isoformat()] = {"week_start": m.isoformat(), "run_km": 0, "runs": 0, "run_min": 0, "long_run_km": 0,
                            "zone_min": collections.Counter(), "hike_km": 0, "hike_elev": 0, "hike_min": 0,
                            "swim": 0, "gym": 0, "run_dates": []}
    m += timedelta(days=7)

def hms(x):
    h, mi, se = map(int, x.split(":")); return h*60 + mi + se/60

for o in summ:
    if o.get("duplicate_of"): continue
    w = weeks[monday(o["date"])]
    w["run_km"] += o["km"]; w["runs"] += 1; w["run_min"] += hms(o["moving"])
    w["long_run_km"] = max(w["long_run_km"], o["km"]); w["run_dates"].append(o["date"][5:10] + " " + o["weekday"])
    for z, mm in (o.get("zone_min") or {}).items(): w["zone_min"][z] += mm
for r in others:
    w = weeks[monday(r["date"])]
    if r["type"] == "Hike":
        w["hike_km"] += r["km"]; w["hike_elev"] += r["elev"] or 0; w["hike_min"] += hms(r["moving"])
    elif r["type"] == "Swim": w["swim"] += 1
    else: w["gym"] += 1

wl = list(weeks.values())
for i, w in enumerate(wl):
    w["run_km"] = round(w["run_km"], 1); w["run_min"] = round(w["run_min"])
    w["hike_km"] = round(w["hike_km"], 1); w["hike_min"] = round(w["hike_min"])
    w["lr_share_pct"] = round(100*w["long_run_km"]/w["run_km"]) if w["run_km"] else None
    zt = sum(w["zone_min"].values())
    w["zone_min"] = {z: round(w["zone_min"][z]) for z in ("Z1", "Z2", "Z3", "Z4", "Z5")}
    w["pct_above_Z2"] = round(100*(w["zone_min"]["Z3"]+w["zone_min"]["Z4"]+w["zone_min"]["Z5"])/zt, 1) if zt else None
    chronic = [x["run_km"] for x in wl[max(0, i-3):i+1]]
    w["acwr_km"] = round(w["run_km"]/(sum(chronic)/len(chronic)), 2) if sum(chronic) else None

(OUT / "runs_summary.json").write_text(json.dumps(summ, ensure_ascii=False, indent=1))
(OUT / "runs_splits.json").write_text(json.dumps(splits_all, ensure_ascii=False))
(OUT / "weekly.json").write_text(json.dumps(wl, ensure_ascii=False, indent=1))
(OUT / "other_activities.json").write_text(json.dumps(others, ensure_ascii=False, indent=1))
(OUT / "workout_laps.json").write_text(json.dumps(laps_out, ensure_ascii=False, indent=1))
print("done", len(summ), "runs", len(wl), "weeks")
