# Knowledge Base: Marathon Training

**Vytvořeno:** 18.9.2026 · **Aktualizováno:** 23.9.2026 (deep analýza všech dat)
**Cílový závod:** Vodafone Prague Marathon, **neděle 2.5.2027**
**Generálka:** Generali Prague Half Marathon, **sobota 3.4.2027**
**Cíl:** sub-3:30 (4:58/km) = ambice (~30–40 %); finální cíl podle PM 3.4.
**Aktuální fáze:** Indonésie 24.9.–11.10. (udržovací), hlavní blok od 12.10.

## Obsah
| Soubor | Obsah |
|---|---|
| 01 | Profil sportovce, historie, tendence |
| 02 | Fyziologie: LTHR, zóny, VDOT, tempa, cíle, rozhodovací prahy |
| 03 | Kompletní tréninkový log (ze Stravy) |
| 04 | Plán do závodu, pravidla, návratový protokol, šablony týdne |
| 05 | Tréninková metodika a principy |
| 06 | Knihovna tréninků a kontrolní časy |
| 07 | Výživa, fueling, hydratace, suplementy, krevní test |
| 08 | Regenerace, volno kolem LR, nemoc |
| 09 | Silový trénink / hybrid |
| 10 | Vybavení, data, cestování |
| 11 | ERRATA — chyby v dřívějším koučování (číst před analýzou) |
| 12 | TODO, monitoring, otázky, kontrolní body, rizika |

## Rychlá fakta
- LTHR = **172 bpm** (30min TT 31.8.2026), max HR ≥181
- VDOT **~40–42** · sub-3:30 potřebuje 44,6
- Easy = **138–153 bpm**, 5:45–6:15/km; prvních 10 min ≥5:45 podle tempa
- Threshold repy = **4:55–5:05/km, konec repu HR ≤168** (ne 4:50)
- Objem před Indonésií: **34–39 km/týden**, 4 běhy · od 26.10. 5 běhů
- Long run max: **16,02 km** (20.9.2026) · pravidlo LR ≤1,10× nejdelšího za 30 dní
- Od restartu 8.5.2026: 444 km, bez běžeckého zranění

## Data ze Stravy
```
python3 scripts/strava.py list --after 2026-09-20   # přehled aktivit
python3 scripts/strava.py detail <id>               # km splity, laps, HR, RPE, popis
python3 scripts/metrics.py --after 2026-09-20       # EF, decoupling, čas nad HR prahy, GAP
```
Přihlašovací údaje v `.env` (gitignored), token se obnovuje sám.
Strava API je zdroj pravdy — neodhadovat z popisu.
