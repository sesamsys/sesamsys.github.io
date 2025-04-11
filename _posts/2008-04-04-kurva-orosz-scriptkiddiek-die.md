---
layout: post
title: kurva orosz scriptkiddiek DIE
author:
  display_name: sesam
  login: sesam
  email: petersz@me.com
  url: http://sesam.hu
date: '2008-04-04 18:00:19 +0200'
date_gmt: '2008-04-04 09:00:19 +0200'
tags:
- hosting
- SQL
- StartLogic
- Tech &amp; Gizmos
comments:
- id: 1136
  author: Youkai
  date: '2008-04-04 20:41:29 +0200'
  date_gmt: '2008-04-04 11:41:29 +0200'
  content: |-
    Reggel próbálkoztam az itunes-ra reagálni, hát nem ment, most már tudom, hogy miért... Amúgy hova akarsz költözni  ? wordpress.com ?
    vagy maradsz még szabadúszó ?
- id: 1137
  author: Vale
  date: '2008-04-04 21:55:08 +0200'
  date_gmt: '2008-04-04 12:55:08 +0200'
  content: de ha ruszki, akkor miért spanyolul van a myspace?
- id: 1138
  author: SeSam
  date: '2008-04-04 22:00:31 +0200'
  date_gmt: '2008-04-04 13:00:31 +0200'
  content: A myspace mindig a te beállításod szerinti nyelven van. Nekem alapban japán.
---

Ha valaki próbálkozott a sesamhuval és nem működött, akkor elnézését kérem. Úgy tűnik a szerver, ahol a siteot elhelyeztem megkapta a magáét. Az SQL adatbázisomban olyan táblák is megjelentek, amelyeket nem én csináltam. Gondolom ennek is köszönhetően (vagy csak szimpla DoS), hasonló hibákat kaptam folyamatosan:

[error] WordPress database error User '***' has exceeded the 'max_questions' resource (current value: 50000) for query SELECT * , IF ...

A dolgot ideiglenesen megoldottam, hogy új felhasználót készítettem más jelszóval, és átírtam a releváns WP beállításokat... De ha ez így megy tovább hosting oldalon, lehet hogy költözés lesz a vége.

Ja, hogy honnan tudom, hogy oroszok? Például [ezt sikerült kinyerni](http://www.myspace.com/1234567_jrl) a parazita táblákból...
