---
layout: post
title: webvideó technoblabla
author:
  display_name: sesam
  login: sesam
  email: petersz@me.com
  url: http://sesam.hu
date: '2008-05-29 16:29:56 +0200'
date_gmt: '2008-05-29 07:29:56 +0200'
tags:
- embed
- mp4
- mplayer
- non-conformity
- QuickTime
- video
- Tech &amp; Gizmos
comments:
- id: 1302
  author: Ardin
  date: '2008-05-29 16:50:05 +0200'
  date_gmt: '2008-05-29 07:50:05 +0200'
  content: Nekem müxik :) (Winfos, FF 3.0, Quicktime, Xvid, DivX codec telepítve)
- id: 1303
  author: SeSam
  date: '2008-05-29 17:28:35 +0200'
  date_gmt: '2008-05-29 08:28:35 +0200'
  content: Vicces, mert én hiába telepítettem winen a QT-t, a FF nem is teszi ki az
    objektumot... Safarin tökéletes.
- id: 1304
  author: oPal
  date: '2008-05-29 19:36:21 +0200'
  date_gmt: '2008-05-29 10:36:21 +0200'
  content: Nah ami tegnap ment csont nélkül, azt most még csak nem is látom. az objektum
    sincs itt.
- id: 1305
  author: SeSam
  date: '2008-05-29 20:11:02 +0200'
  date_gmt: '2008-05-29 11:11:02 +0200'
  content: Jah, ez kevésbé linux-kompatibilis lehet...
- id: 1306
  author: foodlfg
  date: '2008-05-29 20:55:48 +0200'
  date_gmt: '2008-05-29 11:55:48 +0200'
  content: |-
    Lemaradtam valamiről úgy látszik.
    Most hogy nézem, nekem sem jeleníti meg (FF3), de a google readeren keresztül letöltöttem. Szóval úgy megy :P
- id: 1307
  author: SeSam
  date: '2008-05-29 21:00:55 +0200'
  date_gmt: '2008-05-29 12:00:55 +0200'
  content: Nem tudom a Firefox miért nem mutatja. Ez túlmegy az én tudásomon.
- id: 1308
  author: foodlfg
  date: '2008-05-29 22:44:08 +0200'
  date_gmt: '2008-05-29 13:44:08 +0200'
  content: |-
    aha most már jó
    Felajánlotta, hogy telepíteni kéne az epülös lejátszót, amit nem fogok, de legalább már látja, hogy ott van. (:
- id: 1309
  author: Vale
  date: '2008-05-29 23:44:49 +0200'
  date_gmt: '2008-05-29 14:44:49 +0200'
  content: |-
    sayonara... és hogy kiikszelte már a haverját is... ez a scene.
    ebből gondolom következik, hogy látom (winxp, ff2)
---

Németóra van épp, tehát kihasználom az alkalmat, hogy valami hasznosat is csináljak...

Utánanéztem a böngészőben lejátszandó videó problematikájának. A célom az volt, hogy simán <object> tagbe ágyazva a böngésző válasszon magának plug-int, amivel lejátssza. Ilyen pluginja van a WMP-nek ha jól tévedek, Macen a Quicktime épül be a Safariba, linuxon pedig mplayerplug-in látja el ezt a feladatot.

A legnagyobb probléma az [én House-videómmal](http://sesam.hu/2008/05/27/nonkonformitas-es-a-youtube-tartalomellenorzese) az volt, hogy kódoláskor simán beadtam neki egy [lavc](http://en.wikipedia.org/wiki/Libavcodec)-kodeket, ami az [FFmpeg-projekt](http://en.wikipedia.org/wiki/Ffmpeg) része, és FMP4 videót készített belőle. Ezt alapban a QT nem látja. A letöltött avi képe is nagy bazi fehérség volt csak nekem. Macen a [Perian](http://perian.org) nevű ügyes kis kiegészítéssel lehet rábírni a QuickTimeot, hogy az AVI konténerben felismerje az FMP4-et.

Ettől persze még a beépülő meg se moccant nekem, úgyhogy most átkódoltam mp4-be (m4v). Kíváncsi leszek, ez kinek fog menni. ;)

Update: hát persze... a classid-s embed _csak_ IE-kompatibilis (meg úgy látszik a Safarinak jó úgy is), _minden más böngésző_ data taget szeretne. Részletesebben a [Juicy Studio Object Paranoia](http://juicystudio.com/article/object-paranoia.php) oldalán.
