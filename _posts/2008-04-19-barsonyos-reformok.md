---
layout: post
title: bársonyos reformok
author:
  display_name: sesam
  login: sesam
  email: petersz@me.com
  url: http://sesam.hu
date: '2008-04-19 22:52:50 +0200'
date_gmt: '2008-04-19 13:52:50 +0200'
tags:
- design
- flickr
- gallery
- photography
- wordpress
- Tech &amp; Gizmos
comments:
- id: 1185
  author: Youkai
  date: '2008-04-20 01:40:33 +0200'
  date_gmt: '2008-04-19 16:40:33 +0200'
  content: Nah végte flickr user vagy ...  :) gyorsan contact-t lettél :)
- id: 1186
  author: Youkai
  date: '2008-04-20 01:41:42 +0200'
  date_gmt: '2008-04-19 16:41:42 +0200'
  content: Öhh update, mennyi most a sima flicr account limit 200 mega /hó ???
- id: 1187
  author: foodlfg
  date: '2008-04-20 02:07:03 +0200'
  date_gmt: '2008-04-19 17:07:03 +0200'
  content: |-
    Jó sok linket raktál elénk. :D
    Én ezek közül csak a last.fm-et és a del.icio.us-t használom.
    flickr helyett én inkább a google-ös megoldást választottam, de csak azért, mert oda nem kellett külön regisztrálni, kényelmesebb volt.:P

    a cc meg egy jó dolog
- id: 1188
  author: SeSam
  date: '2008-04-21 12:29:54 +0200'
  date_gmt: '2008-04-21 03:29:54 +0200'
  content: |-
    Compare that to what you get with a Free Account:

        * 100 MB monthly upload limit (10MB per photo)
        * 3 sets
        * Photostream views limited to the 200 most recent images
        * Post any of your photos in up to 10 group pools
        * Only smaller (resized) images accessible (though the originals are saved in case you upgrade later)
---

Csak kicsit szembemenve az árral, mondjuk úgy srevizavé, apróbb változásokat foganatosítottam a weboldalon.

Leglátványosabb ugye a kis _social networking_ ikonok megjelenése a címsorban. Gondoltam azt a böszme nagy helyet ki kellene tölteni valamivel. Valamint amúgy is szerettem volna linkeket a [twitteremhez](http://twitter.com/sesam), [facebookomhoz](http://www.facebook.com/profile.php?id=560036693), [last.fmemhez](http://www.last.fm/user/sesamsys). Eddig nem nagyon emlegettem a [technoratit](http://technorati.com/blogs/sesam.hu/WordPress), de oda is regisztráltam már jó ideje. Kár hogy az ismeretségi körömben kevesen használják.

A [del.icio.us](http://del.icio.us/sesamsys) accountomat nemigen használtam eddig, csak szórványosan. Viszont kezdek ráébredni, mennyire hasznos, főleg hogy sokszor idegen (iskolai) gépekre kell szorítkoznom. A blogba később postolandó források tárolására is kiváló.

A legnagyobb változás pedig a [flickr](http://www.flickr.com/photos/sesamsys). Ugye volt arról szó, hogy miért nincs galéria. Nos azért, mert a [StartLogictól](http://www.startlogic.com) kapott kőkori 1.5-ös verziójú [Gallery](http://gallery.menalto.com) nekem nagyon nem jött be. Elárasztották például a gyógyszer- és szexspamek. A flickr pedig _industry standard_ , és gyönyörűen integrálható a WordPressbe.

A gond csak az, hogyan mozgassam át a temérdek képet oda. Nos, [létezik egy plugin](http://gallery2flickr.sourceforge.net), ami a Gallery2 telepítésből átemeli a képeket flickrbe. Egyetlen bibi a dologban, hogy ez 1.x-el természetesen nem működik. Nosza feltettem hát egy újabbat, ami azért nem zajlott ilyen egyszerűen.

Egy telepítés néhány ezer fálj, amit felftpzni közel lehetetlen. Megszakad, kezdi előről, megszakad, szolid hajtépés. Aztán fel lehet tölteni a teljes tömörített galériát, és az adminisztrációs webfelületen kibontatni, ami szintén csak sokadjára sikerült. Végül rettentő sokat szívtam az engedélyekkel is, mire kiderült, hogy alapból rosszul lesznek beállítva, és ezen hasal el a telepítő script. _Long story short_ , kisebb-nagyobb szünetekkel majd' az egész héten ezzel szenvedtem. (Ez a bekezdés még mindig nem igazán írja le azt az orbitális kínlódást, amibe ez nekem került...)

Tehát most van egy ideiglenes Gallery2-m, amibe előbb átemelve az eredetiből a képeket exportálni tudom flickrbe. Ennek tesztje volt a tokiói utamon készült pár kép áthelyezése. Sajnos **nem pro accountok** esetén feltöltési limit is van, amit villámgyorsan el lehet érni. Majd szépen lassan igyekszem átrakni flickrbe is az összes régi képet, kulcsszó a türelem. Vagy valaki megajándékozhat egy pro accounttal némi reklámért cserébe. [Volt már rá példa a világtörténelemben](http://yummie.hu/archives/2007/10/04/you-have-a-flickr-pro-account), de nincsenek illúzióim.

Aki most találkozik először a képekkel, kis caveat: nem vagyok profi, fél- sőt negyedprofi sem. A képek tehát sokszor rosszul komponáltak, rossz az expozíció, fehér az ég, lens flare, stb. Ha valaki szépet akar látni, nézegesse inkább [Adri képeit](http://www.flickr.com/photos/j-adree). Csak azért mondom, mert mostanában **mindenki nagyon komolyan fényképez**.

Természetesen minden kép [cc by-nc-sa](http://creativecommons.org/licenses/by-nc-sa/2.0/deed.en).

Az ikonok [a Gorvan.com hasonlóan szabadon használható szettjéből vannak](http://www.gorvan.com/design/icons/social-website-buttons).

Aki pedig vállalja, hogy leteker az oldal aljáig - és nem mellesleg elolvasta a bejegyzést egészen végig - kis meglepetésben is részesül a [FlickrRSS](http://eightface.com/wordpress/flickrrss) jóvoltából.
