---
layout: post
title: Linkekről
author:
  display_name: sesam
  login: sesam
  email: petersz@me.com
  url: http://sesam.hu
date: '2011-02-24 13:38:03 +0100'
date_gmt: '2011-02-24 12:38:03 +0100'
tags:
- plugin
- security
- wordpress
- spam
- Jun
- script
- checksum
- Akismet
- Tech &amp; Gizmos
comments: []
---

[Merras/Jun írt egy roppant érdekes cikket](http://miyazakijun.hu/keresomarketing/eletveszelyes-wordpress-seo-spamek-amik-kinyirhatjak-a-helyezeseidet.seo) olyan hackekről, amikor a támadók a [WordPress](http://wordpress.org) kódba helyeznek el nemkívánt linkgyűjteményt, nem mellesleg kinyírva ezzel az oldal keresőkben elért helyezését.

Azért éri meg kéretlenül betenni linkeket egy weboldalba, mert a Google például úgy működik, hogy minél többen linkelnek egy oldalra, annál előrébb kerül a találati listában. A logika emögött az, hogy ha sokan irányítanak egy adott oldalra, az valószínűleg releváns információt tartalmaz. Nyilván nem ennyire egyszerű az algoritmus, számít például, hogy az az oldal, amire a link kikerül, maga mennyire rangos, stb., viszont innentől ez egy szakma, amibe nem szeretnék belekontárkodni.

A legalapvetőbb linkbeszúrás kommentben érkezik. Jómagam is [sokat harcoltam](http://sesam.hu/2005/01/24/spambots) a robotok által beküldött néha többszáz linket is tartalmazó kommentek ellen. Szerencsére erre a problémára már [született egy kiváló megoldás](http://sesam.hu/2006/12/06/die-spam-die), az [Akismet](http://akismet.com), ami már jó ideje az alap WordPress telepítés része, és gyakorlatilag kötelező használni.

Ennél szofisztikáltabb megoldás, amikor a WordPress kódjába, például a láblécet generáló PHP fileba, helyeznek el amúgy láthatatlan linkeket. Ehhez elég egy rosszul beállított szerver, egy ellenőrizetlen plugin vagy egy csaló template-site. Pont ezért roppant fontos, hogy megbízható forrásból érkezzenek ezek a kiegészítések, illetve hogy a pluginek és maga a WordPress keretrendszer is rendszeresen legyen frissítve.

Súlyosabb esetben úgy tudnak hatalmas mennyiségű tartalmat beilleszteni keresőmarketing szempontból releváns helyre, hogy az még a mögöttes kód átnézésekor is rejtve marad az oldal tulajdonosa előtt. Ez utóbbi módszer ellen készített TLoF most egy egyszerű scriptet, ami végignézi a WP könyvtár filejait, és checksum adatot generál belőlük. Ilyen módon a legapróbb változás is nyomon követhető, és a támadások kiszűrhetőek.

[A script a Tutorial.hu oldalról tölthető le.](http://www.tutorial.hu/honlap-hackelest-felderito-script) Ezzel kapcsolatban kicsit büszke is vagyok magamra, mert én is hozzájárultam a munkához: találtam bugot a PHP kódban.
