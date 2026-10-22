# Data z aplikace Fitness Hub

Tuhle složku generuje aplikace Fitness Hub každý den (a na tlačítko v Nastavení). **Neupravuj ji ručně** —
další export ji přepíše. Zdrojem pravdy je databáze aplikace; tady je čitelná kopie pro hlubší analýzu.

Pravidla:
- Prázdná buňka = neznámá hodnota, **ne nula**. Den, který v souboru chybí, nemá žádná data.
- Data a časy jsou v místním čase (Europe/Prague). Týdny jsou pondělí–neděle.
- Sekundové streamy běhů tu nejsou — na ně použij `scripts/metrics.py` (Strava API).

Známé mezery v datech:
- **Posilovna 22. 7. – 16. 10. 2026 není zapsaná, ale probíhala**: aspoň 4× týdně, kromě dovolených. Chybějící
  řádky v `gym_*.csv` a nuly v `weeks.csv` za toto období tedy neznamenají pauzu.

Soubory:
- `activities.csv` — všechny aktivity ze Stravy (běh, kolo, plavání, …), jedna na řádek. Tempa v s/km
  (`gap` = tempo upravené o převýšení, Minetti). `ef_gap` = GAP m/min na úder, `decoupling_pct` = GAP/HR první
  vs. druhá polovina ustálené části, `z1_min`–`z5_min` = minuty v zónách podle `lthr_used`. Metriky jen u běhů
  se streamem; `description` je popis ze Stravy (fueling, bolest 0–10).
- `gym_workouts.csv` — tréninky v posilovně; `volume_kg` = váha × opakování pracovních sérií.
- `gym_sets.csv` — každá série. `rir` = opakování v záloze (prázdné = nepotvrzeno), `planned_*`/`role` = plán
  progrese, `unusual` = série mimo progresi. Váha 0 = vlastní váha.
- `nutrition_items.csv` — každá položka jídelníčku s gramy a makry.
- `nutrition_daily.csv` — denní součty (včetně jídla během běhu); `fueling_kcal` = z toho kcal snědené během
  běhu (gely, iont), které se do cíle nepočítají; `items_missing_kcal` = položky bez známých kcal (součet je pak
  podhodnocený).
- `targets_daily.csv` — denní cíl od 21. 10. 2026 do zítřka: `mode` (cut / maintenance / off), `base_kcal`,
  `weight_used_kg` (průměr vážení za 7 dní), `runs` (např. `easy:7.0;long_run_tomorrow:10.0`; odběhnuté km
  nahrazují plánované), `extra_kcal`, `kcal_target` a makra. Dny v režimu `off` cíl nemají. Minulé dny se
  přepočítávají s dnešními daty (např. pozdějším vážením).
- `daily_metrics.csv` — váha, kroky, spánek, klidový tep po dnech. Denní součet kroků pod 50 z hodinek je
  zástupná hodnota (Samsung Health bez hodinek), proto je prázdný.
- `weeks.csv` — týdenní přehled: běh vs. plán z `04_timeline_plan.md`, posilovna, průměrný příjem (jen přes
  dny se záznamem, počet v `nutrition_days`), průměrná váha a kroky.
- `profile.md` — nutriční cíle, vzorec denního cíle a kalendář režimů.
