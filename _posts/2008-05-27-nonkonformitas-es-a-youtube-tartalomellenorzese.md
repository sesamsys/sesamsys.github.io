---
layout: post
title: Nonkonformitás és a Youtube tartalomellenőrzése
author:
  display_name: sesam
  login: sesam
  email: petersz@me.com
  url: http://sesam.hu
date: '2008-05-27 21:19:32 +0200'
date_gmt: '2008-05-27 12:19:32 +0200'
tags:
- fingerprinting
- house
- idiocy
- non-conformity
- youtube
- last.fm
- Human Interest
- Tech &amp; Gizmos
comments:
- id: 1293
  author: SeSam
  date: '2008-05-27 21:56:33 +0200'
  date_gmt: '2008-05-27 12:56:33 +0200'
  content: 'Update: Azt sehogy sem tudom elérni, hogy a beépülő lejátszónak kint legyenek
    a gombjai is. Valamint a Safari+QuickTime egyszerűen nem játssza le. Viszont miután
    két óra alatt sem sikerült megjavítanom, és már nem fogom átkódolni QT movba és
    újra felszenvedni, ez van.'
- id: 1294
  author: Ardin
  date: '2008-05-27 23:17:29 +0200'
  date_gmt: '2008-05-27 14:17:29 +0200'
  content: |-
    Mozilla 3.0 + Quicktime sem akarja megenni. Aszondja valami plugin kellene még hozzá, de ő sem tudja, hogy mi, úgyhogy csak a lejátszó dobozt jeleníti meg (gombok viszont vannak hozzá :) ).

    Igy Járás.
- id: 1295
  author: Youkai
  date: '2008-05-27 23:55:57 +0200'
  date_gmt: '2008-05-27 14:55:57 +0200'
  content: |-
    Nálam is így járás esete forog fent, se FF2.0.0.14+ Quicktime 7 kombóval, se ie 7+ Qt nem eszi meg ie alatt még nem is látszik a kezelőgomb...
    FLV-be esetleg azt elvileg a WP alapból kezeli, vagy valami plug-in vagy out kellet hozzá, most már meg nem mondom. Azt meg nem hiszem, hogy az NBC lecsapna rád, ha meg szívóznak szépen magyar módra 2 nagy tasli, azt ők csendesednek el  :D Én a taslimat a BSA-nak tartogatom, de ha akarod felkajálhatom a köz és a blog érdekében, ha kell irányítsd hozzám őket XD
- id: 1296
  author: SeSam
  date: '2008-05-28 01:39:00 +0200'
  date_gmt: '2008-05-27 16:39:00 +0200'
  content: Igen, mert azt hiszem xvid a codec... mplayerplug-in megeszi, de más nem.
    Bocsánat, de nem volt több energiám vacakolni vele. FLV meg nyilván szuper, de
    nincs semmim, amivel flashbe konvertálnám. Meg fogom csinálni valahogy, eventually.
- id: 1297
  author: Youkai
  date: '2008-05-28 01:59:35 +0200'
  date_gmt: '2008-05-27 16:59:35 +0200'
  content: |-
    Nem kell konvertálni, feltöltöd a videot youtube-ra, s a downloadhelper nevű firefox plugint telepíted előtte, s aztán leszeded a youtube-ról vele, s azonnal van egy flv fájlod, ezek után akár törölheted is a youtube-ről a cuccot, ha az NBC nem gyorsabb ismét nálad :D
    Amúgy megnéztem a videot a segítségével  , nagy :D
- id: 1298
  author: Vale
  date: '2008-05-28 05:06:20 +0200'
  date_gmt: '2008-05-27 20:06:20 +0200'
  content: tölsd föl videa.hu-ra vagy box.netre vagy valami más megosztóra. nem csak
    jútúb van.
- id: 1299
  author: Youkai
  date: '2008-05-28 06:50:20 +0200'
  date_gmt: '2008-05-27 21:50:20 +0200'
  content: Csak gondolom sesam-nak a youtube közelebb van japánból, mint a videa :d
    magyarán ott jó a nemzetközi sávszél az usa felé, de gyík Abszurdisztán felé,
    szóval ha nem akarod a következő képen teljesen kopaszon látni Sesam-ot kezében
    a hajával mit kitépet a várakozás közben, akkor szerintem marad a youtube...
- id: 1300
  author: Human
  date: '2008-05-28 19:25:03 +0200'
  date_gmt: '2008-05-28 10:25:03 +0200'
  content: A beillesztett mpeg (?)  videó padlóra küldte a firefoxot. Safari csak
    hiányolja a plugint, de ez durva így...
- id: 1301
  author: oPal
  date: '2008-05-28 22:47:26 +0200'
  date_gmt: '2008-05-28 13:47:26 +0200'
  content: |-
    nálam minden elsőre ment :-o
    fox 2.0.0.14 + ubuntu valamelyik lejátszója.. valszeg quick-nek köze se lehet ehez :)
---

[Yummien láttam egy modell képét kanjis tetoválással](http://yummie.hu/archives/2008/05/27/gemma-atkinson-a-photoshop-elott), és rögtön a House első szezonja jutott az eszembe, amiből egy jelenetet már régóta szerettem volna postolni. Mert annyira tipikus... amikor először láttam, az üres szobának kezdtem magyarázni, hogy na pontosan _ez_ a bajom a japánfansággal:

**Update:** A [videót a következő postban](http://sesam.hu/2008/05/29/webvideo-technoblabla) lehet - immár remélhetőleg problémamentesen - megtekinteni.

A videót persze először Youtubera szerettem volna kitenni. Érdekes meglepetésként ért, amikor a feltöltés után kábé fél perccel beesett egy email, hogy a szerzői jogok tulajdonosa, az NBC, leszedette a videót azonnali hatállyal. Ezek a fiúk aztán gyorsak, gondoltam, de nem erről volt szó.

Ami engem elkapott, az [a Youtube automatikus tartalomszűrője](http://help.youtube.com/support/youtube/bin/answer.py?hl=en&answer=83766&hl=en_US). Ugyanúgy, ahogy a [musicbrainz](http://wiki.musicbrainz.org/AudioFingerprint?highlight=%28fingerprint%29) vagy a [last.fm](http://blog.last.fm/2007/09/10/fingerprinting-update) [ujjlenyomatozza](http://en.wikipedia.org/wiki/Fingerprint_%28computing%29) a zeneszámokat, úgy ezek a stúdiók is ilyen módszerrel figyeltetik, nem teszi-e valaki közzé ingyen a tulajdonukat. Nagyon cseles...

Érdekes, hogy a FOX nem bánta a [Firefly-részletet](http://sesam.hu/2008/04/26/which-is-your-favourite-tv-show).

Caveat: a beillesztett videó elvileg le kell hogy játszódjon minden modern böngészőben. Ha nem, menj a legközelebbi számítógépes szakértőnek kikiáltott szerencsétlen ismerősöd agyára, hátha segít.

Ha a blog hirtelen elcsendesedne, akkor pedig elvitt az NBC Universal copyright kommandója...
