---
layout: post
title: last.fm fejlesztések
author:
  display_name: sesam
  login: sesam
  email: petersz@me.com
  url: http://sesam.hu
date: '2007-10-07 20:16:29 +0200'
date_gmt: '2007-10-07 11:16:29 +0200'
tags:
- ipod
- itunes
- Mac
- last.fm
- Tech &amp; Gizmos
comments:
- id: 840
  author: bassil
  date: '2007-12-01 22:42:49 +0100'
  date_gmt: '2007-12-01 13:42:49 +0100'
  content: |-
    Szia!

    Régóta Last.fm-ezek, és van egy kis iPos Shuffle-om is... fel is dobja az ablakot, mikor rácsatlakozok a gépre, hogy milyen számokat hallgattam éppen, de ha rámegyek hogy scrobble, akkor last.fm oldalamba csak 1 számot regisztrál be, a többit nemigazán... nemtod hogy mitől lehet?
- id: 841
  author: SeSam
  date: '2007-12-01 22:52:51 +0100'
  date_gmt: '2007-12-01 13:52:51 +0100'
  content: Tudtommal a hivatalos kliens nem támogatja a shuffle-t. Mivel kompakt más
    a playlist-kezelése is.
- id: 842
  author: bassil
  date: '2007-12-02 03:37:39 +0100'
  date_gmt: '2007-12-01 18:37:39 +0100'
  content: Köszi szépen, erre saccoltam énis.
- id: 843
  author: bassil
  date: '2007-12-13 02:37:47 +0100'
  date_gmt: '2007-12-12 17:37:47 +0100'
  content: Az új Last.fm frissítés óta az iPod Shuffle-t is kezeli... hamar megoldódott.
    ;)
---

Nem igazán figyeltem oda a ["hivatalos" last.fm kliensre](http://www.last.fm/download), de egészen szépen fejlesztik. Legfontosabb, hogy most már képes iPod szinkronizálására is, méghozzá sokkal elegánsabban, mint az eddig általam használt [iScrobbler](http://www.last.fm/group/iScrobbler). Az iScrobbler az iTunes _Recently Played_ listáját használja a feltöltéshez ahová ugye az iPod is beteszi a rajta játszott számokat. Ennek a legnagyobb hátránya, hogy amennyiben az iPod után az iTunesban is hallgat valaki zenéket, és csak ezután csatlakoztatja az iPodot, akkor már nem ismeri fel az iScrobbler az iPod zenéit, elveszettnek tekinthetők.

A [last.fm](http://www.last.fm) saját kliense viszont az iPod belő lejátszási listáját figyeli, így nem veszít el számokat. Minden iPod csatlakozáskor feldob egy ablakot a számok listájával, és minden lejátszóhoz külön account is rendelhető. Én mondjuk örülnék egy olyan opciónak, hogy ne kérdezzen rá minden egyes scrobble előtt, hogy valóban akarom-e. Valamint egyelőre olyan a rendszer, hogy hiába játszódtak korábban a zenék az iPodon, a last.fm oldalon elsőként lesznek kilistázva, igaz megfelelő timestamppel.

Mégis, bár _experimental support_ , kiválóan működik. Van Wines verziója is.
