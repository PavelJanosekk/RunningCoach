# Strava dataset — athlete training 8.5.2026 → 23.9.2026

Built 23.9.2026 from the Strava API (source of truth). Do NOT call the Strava API again
(rate limits) — everything is here. Python 3.9 stdlib is available for your own analysis.

## Files
- `runs_summary.json` — one object per Run (59, one is a duplicate: see `duplicate_of`).
- `runs_splits.json` — per-km splits per run: pace, GAP pace, HR, hr_max, elev_diff.
- `weekly.json` — ISO weeks (Mon start): run_km, runs, run_min, long_run_km, lr_share_pct,
  zone_min (run time per HR zone), pct_above_Z2, acwr_km (this week / mean of last 4 incl. this),
  hikes (km, elevation gain, minutes), swims, gym sessions (gym is almost never logged in Strava).
- `other_activities.json` — hikes (big eccentric loads!), swims, 1 gym session.
- `workout_laps.json` — lap data for LTHR test (31.8.), Threshold #1 (8.9.), Threshold #2 (18.9.), strides run (23.9.).
- `streams/<id>.json` — raw per-second streams (time, distance, heartrate, altitude,
  velocity_smooth, cadence, moving, grade_smooth). Use these to compute anything else.

## Field definitions (runs_summary)
- `pace` raw average pace; `gap_pace` grade-adjusted pace (Minetti energy-cost model on grade_smooth).
- HR zones, % of LTHR 172 (from 02_physiology_zones.md): Z1 ≤137, Z2 138–153, Z3 154–162,
  Z4 163–172, Z5 ≥173. NOTE: the KB also defines "Z2+ long run" 143–155 where drift at the end
  is acceptable — so for long runs, time at 154–155 is not automatically a violation.
- `min_above_153` minutes of moving time with HR > 153.
- Steady-state metrics exclude the first 10 min: `ss_hr`, `EF_raw`/`EF_gap` (speed m/min ÷ HR,
  higher = better aerobic efficiency), `decoupling_*_pct` (Friel Pa:HR, first vs second half of the
  post-10-min window; positive = HR drifted up relative to pace). Decoupling is only meaningful for
  steady runs ≥ ~50–60 min; on 5–7 km runs it is dominated by HR still rising and is NOT meaningful.
- `hr_at_gap_6min_km` mean HR while GAP pace was 5:50–6:10/km (post-warm-up, needs ≥5 min in band).
- `gap_pace_at_hr_143_150` mean GAP pace while HR was 143–150 (post-warm-up, ≥5 min).
- `first3km` / `after3km` — pace, GAP, HR, minutes above 153, net elevation. The home route
  (Boskovice) typically starts with a ~50 m descent over the first 3 km and returns uphill.
- `cadence_spm` steps/min (only recorded from 29.8. on; earlier = null).
- HR quality: `hr_dropout_early`, `hr_spike_count`, `hr_p99`. Wrist optical sensor (Samsung
  Galaxy Watch 6) — known to lag and spike; isolated maxima of 182–183 on easy runs are likely artifacts.

## Known context (not in Strava)
- Athlete: male, 29 y, ~83 kg, bodybuilding background, mild caloric deficit, sleeps ~8 h, 10–15k steps/day.
- Restart of running: 8.5.2026 (the KB wrongly says ~July). Half marathon 2:25 in 2025, then detraining.
- Trips: Copenhagen ~30.5., Crete ~8.–13.6. (Samaria Gorge hike), Slovenia 4.–5.7. (hikes, 1721 m D+
  in one day → sore knees ~1 week), hike 8.8. Upcoming: Indonesia 24.9.–12.10., Georgia ski
  22.12.–2.1., Thailand 28.1.–14.2.
- Race: marathon Sunday 2.5.2027 (probably Prague, unconfirmed). Working goal sub-3:30 (4:58/km).
- LTHR test 31.8.: 30 min TT, 6.24 km, avg HR last 20 min = 172.0, pace 4:50 (course downhill first 4 km, uphill last 2).
- Fueling on the 13.9. and 20.9. long runs is unknown. Gels tested once (28.6. 13.19 km, gel after 5 km).
- Gym (upper/lower split) happens but is not logged in Strava.
