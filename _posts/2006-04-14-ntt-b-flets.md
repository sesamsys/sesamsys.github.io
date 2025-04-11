---
layout: post
title: NTT B Flet&#039;s
author:
  display_name: sesam
  login: sesam
  email: petersz@me.com
  url: http://sesam.hu
date: '2006-04-14 15:04:21 +0200'
date_gmt: '2006-04-14 06:04:21 +0200'
tags:
- Tech &amp; Gizmos
comments: []
---

Hogyan veszítsünk el egy szép hosszú bejegyzést: az ember rossz tabon kattint a reload-ra...

Na akkor mégegyszer.

Tehát: magyar billentyűzet, magyar bejegyzés. Megérkezett a netem, még ha kissé döcögősen is. A rendszer továbbra is VDSL, ezúttal 100Mbiten. A különbség az előzőhöz képest, hogy ezúttal egy router - helyi nevén CTU - is került a gép és a VDSL modem közé. (Nem, nem Counter Terrorist Unit, hanem Customer Terminal Unit.) A szerelő jött, látott, beszerelt, aztán bedugta a cuccot a laptopjába, és... semmi sem történt. Ezután mi más következhetett, mint a problémamegoldás Windows-módon: szegény gépet vagy tízszer újraindította, sikertelenül. (Közben következetesen duplán kattintott az ISP bolondbiztos Internet vezérlőpult-féléjének "kattints ide, hogy netezhess, megnyitok neked egy Explorert" gombjára, minek következtében rendszeresen dupla-Explorerek jöttek fel. Néha négy, ha türelmetlen volt.) A vége az lett, hogy közölte, lelép; próbáljam meg én beállítani a saját gépemen, az övé nem működik. Majd visszanéz este.

Beleástam hát magam a dokumentációba. Persze midnen Wines, a kézi beállításhoz meg semmi információt nem írnak le: a felhasználó csak ne kutlászkodjon (tm Ábrahám A.) a routerjében. Ez csak azért furcsa, mert elég sokan használnak Macet errefelé - ők ilyenkor mit csinálhatnak vajon. Próbálkoztam én router IP-kkel hasztalan, mire kiderítettem, hogy a CTU a _https://ctu.fletsnet.com/_ címen érhető el... (Nem, én sem láttam még ilyet...) Na ezt találja ki valaki magától, nem tudom mibe került volna beírni a telepítési útmutatóba... (Úgy jöttem rá, hogy elindítottam a telepítő exe-t cedegán. Aztán az megnyitott egy Firefoxot...)

Felbátorodva, hogy az Azureus boldog zöld mosolygós arcocskákat produkált, gondoltam lehet ebből még szerver is. Aztán kiderült, hogy mégsem, ugyanis az Azu UPnP alapon lett aktív, viszont az Apache nem látszik kintről, ha fejreállok se. A support közölte, nem is fog menni. (Ritka az ilyen kerek elutasítás, valami modern cég lehet ez az NTT.) Annyi halvány reményem van, hogyha az Azu lehet aktív UPnP-vel, akkor az Apache is talán... bár ehhez egyre kevésbé értek. Mindenesetre a portscan eredménye: az összes port _filtered_.

Persze ez nem akadályozza meg az 1MB/s+ letöltési sebességet. (És még nem találtam igazán gyors forrást.) :mrgreen:
