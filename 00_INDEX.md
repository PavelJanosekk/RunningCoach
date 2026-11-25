# Knowledge Base: Marathon Training

**Vytvořeno:** 18.9.2026 · **Aktualizováno:** 25.11.2026 (retest 25.11.: VDOT ~41,2, threshold 4:50–5:00; hubnutí od 23.11. základ 2000; log do 15.11.)
**Cílový závod:** Vodafone Prague Marathon, **neděle 2.5.2027**
**Generálka:** Generali Prague Half Marathon, **sobota 3.4.2027**
**Cíl:** A = **3:40–3:50**, B = sub-4:00 (jistota), 3:30 bonus; dlouhodobě
zlepšovat rychlost. Závodní tempo podle PM 3.4.
**Aktuální fáze:** hlavní blok do 20.12. po tříslu L (27.10., odeznělo):
16.–22.11. 36,4 km (T 4× 1,5 km, LR 13,0), **23.–29.11. lehčí týden s retestem
(✅ 25.11.: VDOT ~41,2 → threshold 4:50–5:00)**, od 23.11. hubnutí (základ 2000);
kyčel L ≤1/10 → kyčle po každém běhu (`09`). Cíl k 20.12. ~45 km / LR ~17 (`04`).

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
- LTHR = **172 bpm** (30min TT 31.8.2026; retest 25.11. bez platného HR), max HR ≥181
- VDOT **~41,2** (retest 25.11.; Daniels 3:44, reálně ~3:46–3:49) · 3:40 potřebuje ~42,5–43
- 188 cm / **83,5 kg** (průměr 9.–15.11.) / ~15 % tuku · **2.–22.11. udržování**
  (základ 2500 → **2650** od 16.11. + běh; 9.–15.11. −0,38 kg), od 23.11. **hubnutí
  do Thajska** (základ **2000**, ověřený udržovací 2500) 0,3–0,5 kg/tý na ~80 kg, kalorie = vzorec v `07`; od 15.2. bez deficitu
- Easy = **138–153 bpm**, 5:45–6:15/km; prvních 10 min ≥5:45 podle tempa
- Threshold repy = **4:50–5:00/km, konec repu HR ≤168** (od 25.11.; cílit na ~4:55)
- Strides 15–20 s, 85–90 % (3:04–3:27 = horní hranice), po rovině / do kopce
- Objem před Indonésií: **34–39 km/týden**, 4 běhy · 5. běh od 30.11.
- Long run max: **16,02 km** (20.9.2026) · pravidlo LR ≤1,10× nejdelšího za 30 dní
- Od restartu 8.5.2026: 571,8 km (76 běhů); problémy: bok hýždě/stehna L
  v červenci (odeznělo, od 1.11. zase mírně), tříslo L 27.10. (odeznělo)

## Data ze Stravy
```
python3 scripts/strava.py list --after 2026-09-20   # přehled aktivit
python3 scripts/strava.py detail <id>               # km splity, laps, HR, RPE, popis
python3 scripts/metrics.py --after 2026-09-20       # EF, decoupling, čas nad HR prahy, GAP
python3 scripts/efficiency.py --after 2026-09-20    # tempo @ HR 147 z rovných ustálených úseků (trend)
```
Přihlašovací údaje v `.env` (gitignored), token se obnovuje sám.
Strava API je zdroj pravdy — neodhadovat z popisu.

## Data z Fitness Hub
`fitness-hub/` = denní export z aplikace sportovce: jídlo (zvážené, úplné),
váha, kroky, posilovna (série, RIR), týdenní přehled. Nejdřív `git pull`,
pak `fitness-hub/README.md`. Ručně neupravovat; prázdná buňka = neznámá hodnota.
