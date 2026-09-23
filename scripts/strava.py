#!/usr/bin/env python3
"""Strava fetch helper. Usage:
  strava.py list [--after YYYY-MM-DD]   summary of activities since date
  strava.py detail <activity_id>        laps, km splits, HR for one activity
"""
import json
import sys
import time
import urllib.parse
import urllib.request
from datetime import datetime
from pathlib import Path

ENV_PATH = Path(__file__).resolve().parent.parent / ".env"
API = "https://www.strava.com/api/v3"


def load_env():
    env = {}
    for line in ENV_PATH.read_text().splitlines():
        if "=" in line and not line.startswith("#"):
            k, v = line.split("=", 1)
            env[k.strip()] = v.strip()
    return env


def save_env(env):
    ENV_PATH.write_text("".join(f"{k}={v}\n" for k, v in env.items()))


def access_token():
    env = load_env()
    if int(env.get("STRAVA_EXPIRES_AT", "0")) > time.time() + 300:
        return env["STRAVA_ACCESS_TOKEN"]
    data = urllib.parse.urlencode({
        "client_id": env["STRAVA_CLIENT_ID"],
        "client_secret": env["STRAVA_CLIENT_SECRET"],
        "grant_type": "refresh_token",
        "refresh_token": env["STRAVA_REFRESH_TOKEN"],
    }).encode()
    with urllib.request.urlopen("https://www.strava.com/oauth/token", data) as r:
        tok = json.load(r)
    # Strava may rotate the refresh token; persist whatever comes back.
    env["STRAVA_ACCESS_TOKEN"] = tok["access_token"]
    env["STRAVA_REFRESH_TOKEN"] = tok["refresh_token"]
    env["STRAVA_EXPIRES_AT"] = str(tok["expires_at"])
    save_env(env)
    return tok["access_token"]


def get(path, **params):
    url = f"{API}{path}"
    if params:
        url += "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"Authorization": f"Bearer {access_token()}"})
    with urllib.request.urlopen(req) as r:
        return json.load(r)


def pace(speed_ms):
    if not speed_ms:
        return None
    s = 1000 / speed_ms
    return f"{int(s // 60)}:{int(round(s % 60)):02d}"


def cmd_list(after):
    ts = int(datetime.strptime(after, "%Y-%m-%d").timestamp())
    acts = get("/athlete/activities", after=ts, per_page=100)
    for a in sorted(acts, key=lambda a: a["start_date_local"]):
        print(json.dumps({
            "id": a["id"],
            "date": a["start_date_local"],
            "name": a["name"],
            "type": a["sport_type"],
            "km": round(a["distance"] / 1000, 2),
            "moving": time.strftime("%H:%M:%S", time.gmtime(a["moving_time"])),
            "elapsed": time.strftime("%H:%M:%S", time.gmtime(a["elapsed_time"])),
            "pace": pace(a.get("average_speed")),
            "hr_avg": a.get("average_heartrate"),
            "hr_max": a.get("max_heartrate"),
            "elev": a.get("total_elevation_gain"),
            "cadence": a.get("average_cadence"),
        }, ensure_ascii=False))


def cmd_detail(act_id):
    a = get(f"/activities/{act_id}")
    out = {
        "name": a["name"],
        "date": a["start_date_local"],
        "description": a.get("description"),
        "rpe": a.get("perceived_exertion"),
        "km": round(a["distance"] / 1000, 2),
        "moving_s": a["moving_time"],
        "hr_avg": a.get("average_heartrate"),
        "hr_max": a.get("max_heartrate"),
        "elev": a.get("total_elevation_gain"),
        "splits_km": [{
            "km": i + 1,
            "dist": round(s["distance"]),
            "pace": pace(s.get("average_speed")),
            "hr": s.get("average_heartrate"),
            "elev": s.get("elevation_difference"),
        } for i, s in enumerate(a.get("splits_metric", []))],
        "laps": [{
            "lap": l["lap_index"],
            "dist": round(l["distance"]),
            "time_s": l["moving_time"],
            "pace": pace(l.get("average_speed")),
            "hr": l.get("average_heartrate"),
            "hr_max": l.get("max_heartrate"),
            "cad": l.get("average_cadence"),
            "elev": l.get("total_elevation_gain"),
        } for l in a.get("laps", [])],
    }
    print(json.dumps(out, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    if sys.argv[1] == "list":
        after = sys.argv[3] if len(sys.argv) > 3 and sys.argv[2] == "--after" else "2026-09-01"
        cmd_list(after)
    elif sys.argv[1] == "detail":
        cmd_detail(sys.argv[2])
    else:
        sys.exit(__doc__)
