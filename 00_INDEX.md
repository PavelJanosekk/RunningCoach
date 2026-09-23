# Knowledge Base: Marathon Training — [USER]

**Vytvořeno:** 18.9.2026 · **Aktualizováno:** 23.9.2026
**Cílový závod:** Maraton, neděle 2.5.2027 (pravděpodobně Praha)
**Pracovní cíl:** sub-3:30 (4:58/km)
**Aktuální fáze:** Indonésie 24.9.–12.10. (udržovací), pak hlavní blok od 13.10.

## Obsah
| Soubor | Obsah |
|---|---|
| 01 | Profil sportovce, historie, kontext |
| 02 | Fyziologie: LTHR, zóny, tempa, testy |
| 03 | Kompletní tréninkový log |
| 04 | Timeline do závodu, bloky, cestovní pauzy |
| 05 | Tréninková metodika a principy |
| 06 | Knihovna tréninků (threshold, long run, strides...) |
| 07 | Výživa, fueling, suplementy |
| 08 | Regenerace |
| 09 | Silový trénink / hybrid split |
| 10 | Vybavení, hydratace, cestování |
| 11 | ERRATA — chyby v dřívějším koučování, opravy |
| 12 | Otevřené otázky / co ověřit |

## Rychlá fakta
- LTHR = **172 bpm** (změřeno 30min TT)
- Threshold tempo = **4:50–4:55/km**
- Easy zóna = **138–153 bpm**, tempo 5:45–6:15/km
- Objem před Indonésií: **34–39 km/týden**, 4 běhy (3 týdny v řadě)
- Long run max dosud: **16,02 km** (20.9.2026)
- Max HR: min. 181 (naměřeno), odhad 185–190 (NETESTOVÁNO)

## Aktualizace dat ze Stravy
```
python3 scripts/strava.py list --after 2026-09-20   # přehled aktivit
python3 scripts/strava.py detail <id>               # km splity, laps, HR
```
Přihlašovací údaje v `.env` (gitignored), token se obnovuje sám.
Strava API je zdroj pravdy pro data v logu — neodhadovat z popisu.