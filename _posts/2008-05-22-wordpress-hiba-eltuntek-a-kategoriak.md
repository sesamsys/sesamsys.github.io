---
layout: post
title: 'WordPress hiba: eltűntek a kategóriák'
author:
  display_name: sesam
  login: sesam
  email: petersz@me.com
  url: http://sesam.hu
date: '2008-05-22 12:34:55 +0200'
date_gmt: '2008-05-22 03:34:55 +0200'
tags:
- malfunction
- StartLogic
- Tech &amp; Gizmos
comments:
- id: 1284
  author: Youkai
  date: '2008-05-22 14:17:01 +0200'
  date_gmt: '2008-05-22 05:17:01 +0200'
  content: |-
    Remélem volt mentésed, én anno ezért húztam el az extra.hu-ról mert mesebeli volt a müködése, tudod, hol volt, hol nemvolt... pedig az ingyenes volt...
    A host üzemeltetőjének már ment e-mail, melyben az édesanyját emlegeted negatív jelzős szerkezetben?
- id: 1285
  author: sld
  date: '2008-05-22 16:09:49 +0200'
  date_gmt: '2008-05-22 07:09:49 +0200'
  content: Read-only az adott mount point ahol ezek a fileok vannak. Lehet RAID vezérlő
    hiba, lemezhiba, de nem akarok találgatni... Elég gáz ez fizetős szerveren.
- id: 1286
  author: SeSam
  date: '2008-05-22 22:02:34 +0200'
  date_gmt: '2008-05-22 13:02:34 +0200'
  content: Hát kurvára örülök neki. Annak meg főképp, hogy semmit sem tudok tenni,
    csak várni, hogy esetleg megjavítják...
- id: 1287
  author: Vale
  date: '2008-05-23 02:20:24 +0200'
  date_gmt: '2008-05-22 17:20:24 +0200'
  content: 'sld: nem kicsit gáz. de nekem még jobb: néha totál leáll az sql, se kép,
    se hang. a cpanel meg olyan sebességgel tölt, mintha dial-upon lennék. na az gáz
    fizetős szerveren.'
---

Nem vagyok ideges.

Először az tűnt fel, hogy a **blogroll nincs a helyén**. Azután összeomlott az egész: **a címkék hiányoznak a bejegyzésekből** , egyúttal **eltűnt az összes kategória** , minden visszanullázódot "uncategorised" alá.

Nem vagyok ideges.

A legrelevánsabbnak tűnő információ, amit a Google kidobott, hogy [indítsam újra az SQL szervert](http://www.top10tech.com/web/2008/03/07/blogging-tips/wordpress/holy-crap-my-wordpress-categories-disappeared). Hát persze.

Közben a phpmyadmin-on keresztül belenéztem az adatbázisba, de az meg ilyeneket köp vissza:

#1 - Can't create/write to file '/tmp/#sql_1301_0.MYI' (Errcode: 13)

Az "Errcode: 13" pedig "permission denied", tehát jogosultsági hiba vagy valami prózaibb: megtelt a lemez.

Mindenesetre remélem, hogy csak ennyi (szar SQL szerver), és nem maradandó a károsodás...

Megismételném: NEM VAGYOK IDEGES

**Update:** Most jó lett. Nálam okosabbak szerint az SQL hiba egy indexfájl írási hibáját jelenti. Tehát az ok feltehetőleg valamilyen filerendszer probléma lehetett: RAID rakoncátlankodás vagy read-only mount point, ilyesmik.
