# ERRATA — chyby v dřívějším koučování a jejich opravy

> Tento soubor je důležitý. Obsahuje tvrzení, která byla během konzultace
> vyřčena chybně a následně opravena. Local AI by je nemělo reprodukovat.

## ❌ "HR 150 je gray zone, zpomal easy běhy na 140–147"
**Oprava:** Nepodložené. Uživatel běhal easy na 142–152 bpm, což je
83–88 % LTHR = **správná easy zóna**. Navíc bylo chybně argumentováno,
že easy 5:20/km @ 150 a long run 6:00/km @ 150 znamená gray zone — ve
skutečnosti průměr long runu nahoru vytáhne cardiac drift v závěru.
Nesrovnatelné hodnoty.
**Platí: 138–153 bpm je easy zóna. Uživatel to trefoval celou dobu správně.**

## ❌ "Potřebuješ 4 týdny base navíc před Fází 2"
**Oprava:** Uživatel splňoval všechna původně stanovená kritéria přechodu
(long run 16 km, objem 35–40 km, 4 běhy, HR se zlepšuje). Nebyl důvod
odkládat. Jediné, co skutečně chybělo, byla **kalibrace threshold tempa**
= otázka jednoho tréninku, ne čtyř týdnů.

## ❌ "Threshold session #1 byl VO2max trénink"
**Oprava:** Nebyl. Avg HR 155–165, max 168–173 = threshold zóna a okolí,
ne 175+. Přesnější zařazení: **10K pace / critical velocity**.
Tempo bylo nad thresholdem, ale HR ukazuje intenzitu jen mírně nad cílem.

## ❌ "Kadence 163 je nízká, je potřeba ji zvýšit"
**Oprava:** 163 byl průměr z celé aktivity včetně rozklusu, výklusu a klusů
mezi repy. Per-lap data ukazují **86 spm per noha = 172 spm celkem**
během intervalů. **Kadence je zcela v pořádku, neřešit.**

## ❌ "Přidej easy run hned v pondělí po long runu"
**Oprava:** Den po long runu = volno nebo aktivní recovery.
Glykogen resyntéza 24–48 h, svalová oprava 48–72 h.
4. běh patří do středu týdne.

## ❌ "Easy run v sobotu před nedělním long runem"
**Oprava:** Den před long runem má být volno nebo max. velmi krátký
recovery jogging. Long run je nejdůležitější trénink týdne.

## ❌ "Běháš jen 3× týdně" / špatné počítání objemu
**Oprava:** Uživatel běhal 4× (Út/St/Pá/Ne). Opakovaně došlo k chybné
interpretaci dat — seskupování běhů z různých týdnů do jednoho.
**Vždy explicitně ověřit, za jaké období jsou data.**

## ❌ Doporučení 200 g proteinu jako optimum
**Oprava:** 200 g = 2,4 g/kg, mírně nad výzkumem podloženým rozsahem
1,6–2,2 g/kg. **170–180 g stačí**, zbytek kalorií lépe do tuků.

## ❌ Odhad jídelníčku na ~1438 kcal
**Oprava:** Uživatel váží jídlo a má reálně 1800–2000 kcal.
Odhad z popisu byl podstřelený. **Vždy se ptát na zvážená data,
ne odhadovat z popisu jídel.**

## ❌ Tvrzení o délce Fáze 1 podle kalendáře
**Oprava:** Číslování týdnů z původního plánu přestalo sedět kvůli
dovoleným a individuální adaptaci. **Používat podmínky přechodu,
ne kalendář.** Adaptace > plán na papíře.

## ⚠️ Nesprávná interpretace "časů intervalů"
Uživatel poslal "4:23 / 4:36 / 4:37 / 4:42" jako časy intervalů —
byla to **tempa v min/km**. Vždy ověřit jednotky matematikou
(vzdálenost × tempo = čas).

## ❌ Data v logu fáze 2 (opraveno 23.9.2026 ze Strava API)
**Oprava:** LTHR test byl **Po 31.8.**, ne ~7.9. "Přechodný týden" míchal
běh ze 7.9. s běhy z 15.–16.9. V logu chyběly běhy 5.9. (+ gym), 9.9.
a long run 15 km 13.9. Max HR během testu bylo 181, ne 173.
**Platí: data od 31.8. v `03_training_log.md` jsou ze Strava API.
Při další aktualizaci stahovat přes `scripts/strava.py`, ne rekonstruovat.**

---

## Metapoučení pro budoucí koučování

1. **Neopravovat to, co funguje.** Uživatel měl easy HR správně celou dobu.
2. **Ptát se na období u dat**, nespojovat běhy z různých týdnů.
3. **Ověřovat jednotky** (tempo vs. čas).
4. **Rozlišovat průměr z celé aktivity vs. per-lap data.**
5. **Nepřidávat překážky bez důvodu** — když kritéria jsou splněna, jít dál.
6. **Nepoužívat odhady, když jsou k dispozici změřená data.**
7. **U easy běhů koukat na per-sekundová/per-km data, ne jen průměr** —
   průměr 148 může schovat 10 min v Z3 (22.–23.9.).