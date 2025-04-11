---
layout: post
title: Babysteps
author:
  display_name: sesam
  login: sesam
  email: petersz@me.com
  url: http://sesam.hu
date: '2006-05-13 11:28:45 +0200'
date_gmt: '2006-05-13 02:28:45 +0200'
tags:
- Tech &amp; Gizmos
comments: []
---

Haladok, ha apránként is. Köszönhetően a WP szuper sablonalapú oldalkezelő rendszerének minimális szenvedéssel áttelepítettem a teljes [portfolio](http://sesam.hu/?page_id=505) szubszekciót. (Milyen szép szó.) Megjegyzem, nem tartott túl sokáig. Nem vagyok túl termékeny mostanság. Egyúttal kijavítottam pár helyesírási hibát is. Érdekes módon mindig találok, akárhányszor is olvasom át. Lehet, hogy titokban szaporodnak.

Időközben szóltak nekem, hogy a Firefox nem négyzeteket, hanem kérdőjeleket pakol a kanjik helyére a megfelelő betűtípus hiányában. Na ettől sem kell megijedni, semmi fontosról nem marad le az, aki nem tud japánul. Valamint az Explorer csak akkor ajánlja fel a betűtípusok telepítését, ha valami beállítás be van kapcsolva, valamint a felhasználó még nem klikkelt a "Never ask again" opcióra. (Az XP egy műveletre jutó átlagos felpattantóablak-szennyezéséből és a saját szokásaimból kiindulva kb. midnenki kikapcsolta, hogy az Explorer ilyeneket kérdezgessen.)

Egyúttal elmesélem, mibe is kerül áttelepíteni a blogot egy elavult rendszerről... Addig rendben van, hogy elmentem szépen a bejegyzéseket tartalmazó SQL táblát és a kommentekét, nade van két probléma: 1) A b2 és a WP struktúrája különbözik, a WB-ben jóval több adminisztratív gezmenc is elmentésre kerül egy bejegyzéssel. 2) A jó öreg b2 szépen ISO-8859-2 kódolással (Latin 2) mentette el postokat, amit WP-be importálva (UTF-8) szépen tönkreteszi az összes ékezetet. Tehát először rá kellett engednem egy iconv-ot az sql-fájlokra. Szerencsémre az iconv gyönyörűen átkonvertálta az egész cuccot pillanatok alatt. (Szegény Winesek, kereshetnek konvertálóprogramot, ami lefogadom nincs is ingyen.) Ezek után beimportáltam az immár Unicode táblákat a WP adatbázisába, majd kézzel átmásoltam a megfelelő oszlopokba a b2 struktúrából a WP struktúrába. Természetesen néhány WP mezőt ki kellett egészíteni a teljes funkcionalitás érdekében. A kategóriákba sorolás megint nagy kihívás volt, ugyanis a bejegyzések táblájában csupán egy számláló van, hogy az adott bejegyzés hány kategóriába tartozik (lehet több is). Egy külön táblában kellett a megfeleltetéseket beállítani, és egy harmadikban a számlálót felülírni, ami az adott kategória összes bejegyzésszámát mutatja. Az egyszerűség kedvéért mindent Uncategorised-ba raktam. Jelenleg 497 post van a sesamhun; nincs az az Isten, hogy én végigmászok mindegyiken egyenként, és bekategorizálom.

A kommentek áttelepítése volt az igazi macera. Addig rendben van, hogy a kommenthez oda vagyon írva, melyik bejegyzésé, nade a bejegyzések táblájában van egy számláló, ami az adott posthoz tartozó kommentszámot mutatja. Ennek hiányában a WP azt hiszi, nincs megjegyzés az adott posthoz, bár rákkatintva látható, hogy van. A probléma tehát, hogy meg kellett keresni, egy adott bejegyzés ID-hez hány komment van, majd ezt a számot beleírni a post-táblázat releváns mezőjébe. Csak úgy tudtam megoldani, hogy egy ideiglenes táblát készíetettem, ahová először kimátrixoltam a bejegyzés ID - kommentszám párokat, majd ezt feleltettem meg a bejegyzés-táblával. Igen, a gyakorlatban is oylan macerás, mint amilyennek hangzik, főleg, hogy sohasem tanultam SQL-t. Ennyi szintaktikai hibát talán C++ programozásra kényszerített tapírok ejtenének, mint én.

De - remélem - sikerült.
