---
layout: post
title: 'Hogyan: reklámmentes Index.hu Safarin'
author:
  display_name: sesam
  login: sesam
  email: petersz@me.com
  url: http://sesam.hu
date: '2007-08-24 13:51:25 +0200'
date_gmt: '2007-08-24 04:51:25 +0200'
tags:
- Tech &amp; Gizmos
comments:
- id: 759
  author: foodlfg
  date: '2007-08-24 16:17:26 +0200'
  date_gmt: '2007-08-24 07:17:26 +0200'
  content: |-
    Én azt hallottam, hogy Japánban is megy az arcba reklámozás, talán még jobban is mint itt. (megerősítés szükségeltetik) Azért már igazán immúnissá válhattál volna.
    Pl japán zenei műsort néztem és ott nem is mentek el reklámra, hanem közvetlenül a műsorba szúrták be a reklámot és közben a háttérben meg mutogatták a vendégeket, akik erőltetett (kis túlzás) arccal próbáltak mosolyogni, meg különféle dolgokat csinálni, hogy legyen valami látvány is.
    Nekem ez úgy megy, hogy látok egy reklámot és két perc múlva arra sem emlékszem, hogy melyik cég reklámja volt, nem hogy mit reklámozott. Mondjuk a net abból másabb, hogy itt könnyebb blokkolni (és ha lehet akkor miért ne?), de engem annyira nem zavarnak, hogy ezért plug-in-eket telepítgessek..

    Ez az indexes fenyegetőzés meg egy vicc :)
- id: 760
  author: SeSam
  date: '2007-08-24 16:33:23 +0200'
  date_gmt: '2007-08-24 07:33:23 +0200'
  content: |-
    Csk azt hiszed hogy nem emlékezel. Az emberek ennél bonyolultabban működnek.

    Japán létem alatt összesen ha 2-3 óra TVt néztem eddig...
- id: 761
  author: Youkai
  date: '2007-08-24 17:03:55 +0200'
  date_gmt: '2007-08-24 08:03:55 +0200'
  content: |-
    Ja, tudat alatti reklám a leggázabb, amit simán bárki összehoz, ha tv alatt alszik el ...
    Amúgy én ahogy robban a balhé a zindexel reptéban blokkoltam a hírdetéseiket,  firefox  thx.. szóval érdemes most hihetetlenül gyors az index
- id: 762
  author: foodlfg
  date: '2007-08-24 17:09:43 +0200'
  date_gmt: '2007-08-24 08:09:43 +0200'
  content: Valami olyasmire gondolsz, hogy tudat alatt ez valamilyen módon rögzül
    és ott fejti ki a hatását ? Hát lehet, de nem emlékszem olyasmire, hogy pl  azért
    vettem volna meg valamit, mert többet láttam a reklámját, vagy mert ismerősebb
    lett volna az a termék, mint a másik.. Inkább megpróbáltam mindig utánajárni,
    hogy melyik lehet nekem a jobb.
- id: 763
  author: Youkai
  date: '2007-08-26 04:21:36 +0200'
  date_gmt: '2007-08-25 19:21:36 +0200'
  content: |-
    Persze, de volt anno a nagy "kalapos" kisérlet, vagy csak a Fight Club efektjei ... Hófehérke, a 7 törpe meg egy nem törpe  ... :)
    Amúgy müködik volt amerikában egy kutatás, hogy jólakott diákoknak vetítettek egy filmet,  amiben valami édesség volt, a film után meg kívánták azt a kaját.... Aztán a helyi hatóságok be is tílották a dolgott
---

Na, csak mert ilyen kis aktívkák az ötbetűs portálnál, gondoltam szólok, a hosts file átírásával értelemszerűen a Safari sem mutatja többé az Index reklámjait. Csupán a következő két sort kell elhelyezni az /etc/hosts fileban:

`127.0.0.1 sher.index.hu  
127.0.0.1 rehs.index.hu`

És violá:

[![Index.hu without ads \(thumbnail\)](http://www.sesam.hu.php5-19.dfw1-2.websitetestlink.com/wp-content/uploads/2007/08/index-noad-thumb.jpg)](http://www.sesam.hu.php5-19.dfw1-2.websitetestlink.com/wp-content/uploads/2007/08/index-noad.png "Index.hu without ads")

Lehet perelni.
