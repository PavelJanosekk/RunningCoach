# Data z aplikace Fitness Hub

Tuhle složku generuje aplikace Fitness Hub každý den (a na tlačítko v Nastavení). **Neupravuj ji ručně** —
další export ji přepíše. Zdrojem pravdy je databáze aplikace; tady je čitelná kopie pro hlubší analýzu.

Pravidla:
- Prázdná buňka = neznámá hodnota, **ne nula**. Den, který v souboru chybí, nemá žádná data.
- Data a časy jsou v místním čase (Europe/Prague). Týdny jsou pondělí–neděle.
- Sekundové streamy běhů tu nejsou — na ně použij `scripts/metrics.py` (Strava API).

Soubory:
- `activities.csv` — všechny aktivity ze Stravy (běh, kolo, plavání, …), jedna na řádek. Tempa v s/km
  (`gap` = tempo upravené o převýšení, Minetti). `ef_gap` = GAP m/min na úder, `decoupling_pct` = GAP/HR první
  vs. druhá polovina ustálené části, `z1_min`–`z5_min` = minuty v zónách podle `lthr_used`. Metriky jen u běhů
  se streamem; `description` je popis ze Stravy (fueling, bolest 0–10).
- `gym_workouts.csv` — tréninky v posilovně; `volume_kg` = váha × opakování pracovních sérií.
- `gym_sets.csv` — každá série. `rir` = opakování v záloze (prázdné = nepotvrzeno), `planned_*`/`role` = plán
  progrese, `unusual` = série mimo progresi. Váha 0 = vlastní váha.
- `nutrition_items.csv` — každá položka jídelníčku s gramy a makry.
- `nutrition_daily.csv` — denní součty; `items_missing_kcal` = položky bez známých kcal (součet je pak podhodnocený).
- `daily_metrics.csv` — váha, kroky, spánek, klidový tep po dnech.
- `weeks.csv` — týdenní přehled: běh vs. plán z `04_timeline_plan.md`, posilovna, průměrný příjem (jen přes
  dny se záznamem, počet v `nutrition_days`), průměrná váha a kroky.
- `profile.md` — nutriční cíle a základní údaje.
