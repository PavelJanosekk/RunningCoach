# Výživa

## Aktuální stav (10/2026) — záměrné hubnutí do Thajska

**Rozhodnutí sportovce 21.10.2026:** vysekat se do odletu do Thajska (28.1.2027),
pak udržovat nebo nabírat podle potřeby. „Necílit na hubnutí“ a „deficit
není“ (i v errata `11`) popisují stav 9/2026 — od 21.10. je deficit záměrný.

**Změřeno 14.–20.10.** (Fitness Hub, zvážené, log úplný vč. víkendu):
průměr **2004 kcal**, bílkoviny 171 g (2,1 g/kg), sacharidy **197 g (2,4 g/kg)**,
tuky 58 g, vláknina 28 g.
**Váha:** **82,5 kg** (17.–20.10., 4 vážení; v 9/2026 ~85) · 188 cm · tuk ~15 % (odhad)
Jídelníček, váha a kroky po dnech: `fitness-hub/` (denní export z aplikace).

## Hubnutí do Thajska (21.10.2026–27.1.2027)
| Co | Jak | Proč |
|---|---|---|
| Tempo | **0,3–0,5 kg/tý** 7denního průměru (~0,5 % váhy) | sportovci s ~1,4 % váhy/tý ztratili výkon, s ~0,7 % ne a přibrali sval (Garthe 2011) |
| Kalorie | **vzorec níže** = základ + běh | deficit hlavně ve dny bez běhu, klíčové tréninky nakrmené |
| Bílkoviny | **175 g** fixně | 2,1 g/kg drží sval i v deficitu; 200 g nic nepřidá |
| Tuky | **50 g** fixně (minimum ~0,6 g/kg) | hormony, vitamíny A/D/E/K — níž ne |
| Sacharidy | **zbytek** kalorií | všechno navíc za běh jde do sacharidů |
| Cíl | **~78–80 kg**, níž ne | při stejné svalové hmotě ~11–12 % tuku |

**Fáze:**
- **21.10.–20.12.:** deficit podle vzorce (objem 26 → 55 km).
- **Gruzie 21.12.–3.1.:** udržovací (pauza v hubnutí) — lyže + výška, těžko
  se loguje. Dvoutýdenní pauza výsledek nezhorší (MATADOR 2018, i když u obézních).
- **4.–27.1.:** deficit podle vzorce (objem 32 → 52 km).
- **Thajsko 28.1.–14.2.:** jíst do sytosti, nepočítat.
- **Od 15.2. (maratonský blok):** **žádný deficit** — udržovat nebo nabírat.
  Startovní základ ≈ poslední základ + ~500 kcal, pak ladit podle váhy.

**Varovné signály nízké energie** (přebíjí váhu → hned +200 kcal do základu):
klidová HR ráno +5 bpm držící se týden, easy tempo při stejné HR horší o
>10 s/km a cutback nepomůže, pokles libida, opakované nemoci, lokální bolest
kosti, únava neodchází po cutbacku.

## Vzorec denních kalorií (pro Fitness Hub)
```
navíc(běh) = k × váha_kg × km          váha = 7denní průměr
  k = 0,75   easy, strides, kopce
  k = 1,0    threshold a long run (klíčové tréninky)

kcal_den = základ
         + navíc(běhy dnes, kromě LR)
         + ½ navíc(LR dnes) + ½ navíc(LR zítra)

základ = 2000 kcal (den bez běhu, posilovna +0)
bílkoviny 175 g · tuky 50 g · sacharidy = (kcal − 700 − 450) / 4
zaokrouhlit na 50 kcal
```
- **Lineárně podle km:** čistá cena běhu je ~0,9–1,0 kcal/kg/km skoro
  nezávisle na tempu → 15 km stojí 3× víc než 5 km, ne méně za kilometr.
- **k = 0,75 u easy** vrátí ~80 % ceny běhu; deficit pak s objemem roste
  jen pomalu. **k = 1,0 u klíčových** — deficit na nich stojí kvalitu.
- **LR napůl:** ½ den předem (glykogen na start), ½ v den LR (regenerace).
  Den před LR je volno, takže základ + ½ LR.
- **Fueling během běhu** (iont, med, želé, gely) jde **navíc nad cíl** — nešetřit.
- **Jídlo před během** (víc sacharidů den před LR, rýžové chlebíčky před LR)
  zapisovat jako normální jídlo, ne fueling: na to je ½ LR v cíli den předem
  a v den LR. Jako fueling jen to, co se sní během běhu.
- km = plánované běhy; po běhu nahradit skutečnými km ze Stravy (jen pro dnešek).
  LR a threshold podle plánu v `04` (`weeks.csv`: `plan_long_run`, `plan_quality`).
- Odpovídá dřívějšímu pravidlu „+10 km/tý ≈ +120 kcal/den“.

**Příklady při 82,5 kg** (easy ~62 kcal/km, LR/T ~83 kcal/km):
| Den | kcal | sacharidy |
|---|---|---|
| bez běhu | 2000 | ~210 g (2,6 g/kg) |
| easy 5 km | 2300 | ~290 g (3,5 g/kg) |
| easy 7 km | 2450 | ~325 g (3,9 g/kg) |
| threshold 10 km vč. rozklusu | 2850 | ~425 g (5,2 g/kg) |
| den před LR 10 km / den LR | 2400 / 2400 | ~310 g (3,8 g/kg) |
| den před LR 14 km / den LR | 2600 / 2600 | ~360 g (4,4 g/kg) |
| den před LR 20 km / den LR | 2850 / 2850 | ~425 g (5,2 g/kg) |

Týden 19.–25.10. podle vzorce: Po 2000 · Út 2350 · St 2450 · Čt 2000 ·
Pá 2300 · So 2400 · Ne 2400 → průměr ~2270 kcal (14.–20.10. reálně 2004).

**Ladění základu** — každé pondělí od 9.11. (do té doby váhu zkresluje
glykogen z vyšších sacharidů, +0,5–1,5 kg): tempo = změna 7denního
průměru za 2 týdny ÷ 2.
| Tempo hubnutí | Základ |
|---|---|
| > 0,6 kg/tý | +150 kcal |
| 0,2–0,6 kg/tý | beze změny |
| < 0,2 kg/tý nebo roste | −100 kcal (minimum 1900) |

## Sacharidy
Změřeno 14.–20.10.: **197 g/den (2,4 g/kg)**, rozptyl 96–327 g; St–So jen
96–157 g. (Dřívější „~240–250 g“ byl dopočet, menu z 9/2026 dávalo ~110–130 g.)

| Období | Běžný den | Kvalita | LR den + den před LR |
|---|---|---|---|
| Hubnutí 21.10.–27.1. (kromě Gruzie) | podle vzorce: 2,6 g/kg bez běhu, 3,5–4 g/kg s easy | ~5 g/kg | ~4–5,5 g/kg (vzorec) + fueling navíc |
| Gruzie 21.12.–3.1. | udržovací, do sytosti | — | — |
| Maratonský blok | průměr 5–7 g/kg | | 7–8 g/kg u LR ≥26 km |
| Závod | carb-load 36–48 h: 8–10 g/kg (660–830 g/den), málo vlákniny | | |

Prakticky: 500 g zeleniny + 500 g kuřete denně hodně zasytí → v klíčové dny
část zeleniny vyměnit za rýži / těstoviny / brambory / pečivo, přidat banány,
džus, med. 30–60 g sacharidů před thresholdem.

## Tuky
Pod ~0,6 g/kg ne (hormony, vitamíny A/D/E/K, omega-3). **Při hubnutí 50 g**
(14.–20.10. průměr 58 g), **od 15.2. 60–70 g**. Sacharidy kvůli tukům nesnižovat.

| Kde | Co přidat | Δ tuk | Δ kcal |
|---|---|---|---|
| Snídaně | 2 celá vejce | +10 g | +140 |
| Oběd | 1 lžíce olivového oleje | +14 g | +120 |
| Večeře | olej / kuřecí stehna místo prsou | +14 g | +120 |
| Svačina | 30 g ořechů | +15 g | +180 |

Zdroje: vejce, tučné ryby (losos, makrela, sardinky; bonus omega-3), ořechová
másla, avokádo, plnotučný řecký jogurt, sýry, ořechy.

## Protein
**175 g (2,1 g/kg)** i při hubnutí — výzkum 1,6–2,2 g/kg. Víc nepotřeba
(cíl 200 g ve Fitness Hub snížit).

## Váha a složení těla
- 188 cm / 82,5 kg (10/2026) / ~15 % tuku (odhad) → hubnutí do Thajska
  na **~78–80 kg**, tempo a fáze viz výše. Každý kg dolů ≈ až ~2,5 min na
  maratonu, ale nikdy za cenu tréninku.
- V deficitu drží sval **váha na čince, ne objem** (`09`).
- Horní polovina těla na údržbě do 2.5. — další svalová hmota nahoře = kg navíc.
- Více sacharidů = +1–2 kg glykogenu a vody za první týden. Není to tuk.
- V závodním týdnu nevážit (carb-load = +1–2 kg).

## Post-workout
40–60 g sacharidů + 30–40 g proteinu do hodiny po tréninku (glykogen,
proteosyntéza, kortizol).

## Jídlo před během
| Běh | Co |
|---|---|
| <60–75 min | nic nutné |
| 75–90 min | lehké jídlo 1,5–2 h před (banán + vločky, toast s medem) |
| LR ≥18 km | 1–1,5 g/kg (80–120 g sacharidů) 2–3 h před, nebo 40–60 g jednoduchých sacharidů, když vybíháš do 60–90 min |

Minimum tuků a vlákniny před během. Broskev + nektarinka (~20–25 g) stačí na
běhy do ~100 min, na 2 h+ je to málo.

## Fueling během běhu — cíl v g/h
Maraton při 83 kg ≈ 3500 kcal, z toho ~570–740 g ze sacharidů. Bez
**60–90 g/h** během závodu zásoby nestačí. Glykogen v horní polovině těla
nohám nepomůže.

**Trénink střeva** — střevo se adaptuje na **množství sacharidů/h, ne na
formu** → do února levné zdroje, od března závodní gely (8–9 týdnů na
zvyknutí žaludku na konkrétní produkt stačí).
| Období | LR | g/h | Z čeho |
|---|---|---|---|
| do 15.11. | 7–16 km (<1:45 h) | 0–30 (volitelně) | voda / DIY iont |
| 16.11.–prosinec | 17–22 km | 45–60 | DIY iont 500 ml + med / želé |
| Leden–únor | 18–22 km | 60 | dtto, víc |
| **Od března** | 24–30 km | 60–90 i v MP úsecích | **gely** (závodní produkt); carb-load zkouška před PM a peak LR |

**Levné zdroje (do února):**
| Zdroj | Sacharidy |
|---|---|
| **DIY iont:** 500 ml vody + 30–40 g cukru / maltodextrinu + špetka soli | 30–40 g (6–8 % = nejlepší vstřebávání) |
| Med (lžíce / malá lahvička) | ~17 g / lžíce |
| Gumoví medvídci / želé | ~75 g / 100 g (10 ks ≈ 20 g) |
| Naředěný sirup | podle ředění |
| Datle, banán | 15–25 g / ks (víc vlákniny, jen v easy tempu) |

Cukr (sacharóza) = půl glukóza, půl fruktóza → stejná směs jako drahé gely
pro vyšší dávky. Maltodextrin ve velkém balení = pár Kč na běh.
**Příklad LR ≥17 km:** 500 ml DIY iontu (~40 g) + 10–15 medvídků nebo
1–2 lžíce medu kolem 50.–60. min → ~45–60 g/h.

Nad 60 g/h je potřeba směs glukóza + fruktóza. Gely nekonzumovat naráz,
zapíjet (kromě isotonických). **Nikdy nic poprvé na závodě.**
✅ Gel otestován 1× (28.6.), žaludek OK.
**Teď:** na LR žádné gely, vesta s ≤250 ml vody — do ~100 min stačí.
Od LR ~17 km (>1:45 h) začít se sacharidy podle tabulky (DIY iont, med,
želé) a nosit ~500 ml; gely až od března.
Maraton na 3:40–3:50 = ~3,7–3,9 h → fueling je ještě důležitější než při 3:30.

**Fueling log:** u každého běhu ≥75 min jeden řádek do popisu na Stravě —
snídaně (g sacharidů, kdy), gely (minuty), ml, sodík, GI 0–3.

## Závod
- Snídaně 1–2 g/kg (80–160 g sacharidů) 2,5–3 h před startem.
- 60–90 g/h (~8–12 gelů po 25 g), sodík 300–600 mg/h.
- Pít podle žízně ~400–800 ml/h, **nikdy >1 l/h**.
- **Kofein:** 3 mg/kg (~250 mg) ~60 min před, nebo 150–200 mg před + 100 mg
  gel na km 25–30. Otestovat na MP LR v březnu a na PM.

## Hydratace a sodík
| Délka / podmínky | Co |
|---|---|
| <90 min, chladno | voda |
| 90+ min nebo horko | elektrolyty (sodík) |
| Horko (Indonésie, Thajsko) | 60–90 min před během 500 ml s 300–600 mg Na; běh >45–50 min nést 500 ml |

- **Domácí iont: ¼ lžičky soli + lžíce medu + citron do 500 ml (~575 mg Na).**
  "Špetka" (~250–300 mg/l) je moc slabá — pot má typicky ~900–1000 mg Na/l.
- Po běhu v horku: 1,25–1,5 l na každý kg ztráty, se sodíkem, během 2–4 h.
  Celkem 3–5 l/den, světle žlutá moč.
- **Sweat test:** váha nahý, osušený před a po běhu; pot l/h = (před − po +
  vypito) / hodiny. Indonésie 28.9.–4.10., pak v listopadu a na jaře.
- Stop a zchladit se: závrať, zimnice / husí kůže v horku, zmatenost,
  přestane se potit.

## Suplementy
| Suplement | Dávka | Pozn. |
|---|---|---|
| **Vitamin D3** | 1000–2000 IU s jídlem od listopadu | pokud 25(OH)D není >100 nmol/l; upravit podle února |
| **Kofein** | 3 mg/kg na závod | viz Závod |
| Kreatin | 3–5 g/den | volitelný; +0,5–1,5 kg vody (zkresluje váhu při hubnutí); zvážit vysazení ~4–6 týdnů před závodem |
| Omega-3 | 2–3 g/den | nízká priorita, pokud 60–70 g tuku a ryby 2×/tý |
| Hořčík | 300–400 mg večer | nízká priorita; glycinát / malát, ne oxid |
| Železo | **jen podle krevního testu a lékaře** | muž naslepo nebrat |

Zbytečné: BCAA, glutamin, předtréninkovky, kloubní výživa.

## Krevní test — Čt 5.11.2026 ráno nalačno
Odloženo z 15.10. kvůli rýmě (20.10. ještě mírná, proto ne 29.10.).
Ne do ~2 týdnů po infekci a ne den po LR / kvalitě — zánět i tvrdý trénink zvedají feritin a CRP (feritin by vyšel
falešně dobrý).
KO, ferritin, saturace transferinu, 25(OH)D, CRP + **testosteron, TSH, fT3**
jako výchozí hodnota — od 21.10. záměrný deficit a při nízké energetické
dostupnosti klesají první (srovnání, kdyby přišly varovné signály). Ferritin <30–35 µg/l = pro
vytrvalce relevantní deficit. Hraniční hodnoty zopakovat v půlce února.
