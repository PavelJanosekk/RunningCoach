# Deep analýza 9/2026 — průběh

Cíl: hloubková analýza všech dat (Strava 8.5.–23.9.2026 + KB) → report
`deep_analysis_2026-09.md`. Každá oblast: analýza → ověření (přepočet z dat,
hledání protiargumentů) → kritika → syntéza do reportu. Bez subagentů.

- Data: `data/` (odvozené metriky, popis v `data/README.md`; per-sekundové
  streamy v `data/streams/` jsou jen lokálně, gitignored).
- Surové nálezy analytiků: `raw/lens_*.json`.

## Stav
| # | Oblast | Analýza | Ověření | Kritika | Syntéza |
|---|---|---|---|---|---|
| 1 | Výživa, fueling, síla, regenerace (fuel) | ✅ | ✅ | ✅ | ✅ |
| 2 | Zátěž a riziko zranění (load) | ✅ | ✅ | ✅ | ✅ |
| 3 | Aerobní vývoj a reálnost cíle (aerobic) | ✅ | ✅ | ✅ | ✅ |
| 4 | Kritika plánu do závodu (plan) | ✅ | ✅ | ✅ | ✅ |
| 5 | Intenzita a provedení (intensity) | ⬜ | ⬜ | ⬜ | ⬜ |
| 6 | Audit KB vs data, monitoring (audit) | ⬜ | ⬜ | ⬜ | ⬜ |
| 7 | Finální kritika napříč oblastmi + TL;DR | ⬜ | | | |

## Jak navázat po přerušení
Otevři tento soubor, najdi první ⬜ a pokračuj. Ověřené nálezy každé oblasti
jsou v reportu v její sekci; nic dalšího není potřeba.
