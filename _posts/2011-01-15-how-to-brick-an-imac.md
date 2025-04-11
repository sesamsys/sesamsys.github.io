---
layout: post
title: How to brick an iMac
author:
  display_name: sesam
  login: sesam
  email: petersz@me.com
  url: http://sesam.hu
date: '2011-01-15 13:58:18 +0100'
date_gmt: '2011-01-15 12:58:18 +0100'
tags:
- apple
- brick
- freeze
- iMac
- kernel
- life
- QQ
- Tech &amp; Gizmos
comments:
- id: 2321
  author: Vale
  date: '2011-01-15 14:03:24 +0100'
  date_gmt: '2011-01-15 13:03:24 +0100'
  content: nem garanciális már?
- id: 2322
  author: SeSam
  date: '2011-01-15 15:26:12 +0100'
  date_gmt: '2011-01-15 14:26:12 +0100'
  content: Már több mint egy éve nem az.
- id: 2323
  author: sld
  date: '2011-01-15 16:57:46 +0100'
  date_gmt: '2011-01-15 15:57:46 +0100'
  content: Szerezni egy OSX installer DVD-t és arról bootolva újrahúzni nem megy?
- id: 2324
  author: SeSam
  date: '2011-01-15 17:47:52 +0100'
  date_gmt: '2011-01-15 16:47:52 +0100'
  content: Írtam, hogy nem bootol CD-ről. Egyébként van OS X DVD-m, kettő is.
- id: 2325
  author: Youkai
  date: '2011-01-15 19:54:10 +0100'
  date_gmt: '2011-01-15 18:54:10 +0100'
  content: Szerintem próbáld az i-doki-nál 20.k HUF  körül írják az imac csíkozás
    javítását. Mondjuk, ha ez még laptop alkatrészekből van egy kis takarítás és újrapasztázás,
    néha csodákra képes.
- id: 2326
  author: sld
  date: '2011-01-16 11:44:12 +0100'
  date_gmt: '2011-01-16 10:44:12 +0100'
  content: |-
    Shit, azt nem lattam. :(
    Ja, iDoki jellegű helyek talan tudnak segiteni.
- id: 2327
  author: SeSam
  date: '2011-01-16 11:51:26 +0100'
  date_gmt: '2011-01-16 10:51:26 +0100'
  content: Még egy lehetőség a Target Disk Mode, de nincs hozzá itt Firewire kábelem,
    a laptophoz meg töltőm... meg kell várni tesómat...
---

A mai nap tanulsága: az ember ne játsszon a kernel extensionökkel, avagy hogyan tegyünk tönkre egy iMacet.

A hozzám hasonlóan [állandó grafikai fagyásokkal](http://sesam.hu/2010/11/04/24-imac-screen-freeze) megáldott iMac felhasználók titkon azért reménykedtek, hátha belecsempésznek egy javítást a 10.6.6 frissítésbe. Nem így történt: ma délelőtt kétszer egymás után változatos színűre fagyott a kijelző.

Az Apple Support fórumon egy csávó azt állítja, hogy a 10.6.2-es patchből kioperált meghajtókkal neki sikerült megszüntetnie ezt az iszonyatosan bosszantó jelenséget. [Csupán három kernel extensiönt kell kicserélni...](http://discussions.apple.com/message.jspa?messageID=12895464#12895464)

A meghajtók lecserélése után az iMac megragadt az alma logós boot forgó kerekénél. Újraindítottam parancssoros módban, és visszacseréltem az ATI2600 kext filet. A support és framebuffer meghajtók a régiek maradtak. Lehet, hogy itt követtem el a hibát. Vagy ott, hogy nem használtam a [kext helpert](http://cheetha.net).

Ugyanis ettől a pillanattól fogva **az iMac nem bootol, bármit csinálok vele**. SMC reset nem segít, NVRAM reset nem segít. NVRAM reset háromszor egymás után nem segít. Safe modeba sem bootol, CD-ről sem bootol. Tritone, és fehér/szürke képernyő. Ennyit tud a gép jelenleg.

Tesóm hazavitte a MacBook töltőmet, a laptopon meg jó ha 5% akkuidő maradt. (A sajátjának elégette a vezetékét. Don't ask.) Az ubuntu szerveremhez nincs monitorom. Most ~~elloptam~~ kölcsönvettem tesóm monitorját és billentyűzetét, úgy írom ezt a bejegyzést.

Kissé kétségbe vagyok esve. Az iMacet javítani valószínűleg többhavi fizetésem lenne. Ötletem sincs, mit csináljak.

**Update:** Kipróbáltam a Target Disk Modeot, természetesen nem működik. Az elején azt hittem, abszolút semmit sem csinál, de pár perc állás után megjelent a Firewire ikon. Csak épp a hoszt gép nem lát belőle semmit. Ha kihúzom majd bedugom a vezetéket, akkor pedig ezt írja a konzol:

Jan 17 18:34:30 Snowflake SystemUIServer[112]: ICANotifications framework timed out waiting for a FireWire device with GUID '9907699246124904' to become ready!

A furcsa az iMac viselkedésében az, hogy az amúgy a képernyő szélei között pattogó Firewire ikon (megnéztem, hogy kellene kinéznie a MacBookon) percenként ugrik egy framet. Mintha valami működésképtelenre lassítaná a gépet.

Ugyanez a CD is. Nem bootol az OS X DVD-ről, de vagy öt percig szenved magában, mire kiadja a DVD-t. Erre is véletlenül jöttem rá, amikor egyszer dühömben úgy hagytam.

Egyre gyanúsabb, hogy ez nem szimpla HDD probléma, és keresztet vethetek az egész gépre.
