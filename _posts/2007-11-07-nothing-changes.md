---
layout: post
title: Nothing changes
author:
  display_name: sesam
  login: sesam
  email: petersz@me.com
  url: http://sesam.hu
date: '2007-11-07 11:55:49 +0100'
date_gmt: '2007-11-07 02:55:49 +0100'
tags:
- fud
- index
- Mac
- osx
- trojan
- Tech &amp; Gizmos
comments:
- id: 912
  author: Youkai
  date: '2007-11-07 12:04:50 +0100'
  date_gmt: '2007-11-07 03:04:50 +0100'
  content: |-
    Mondjuk, én amikor anno osx86-al szórakoztam, annyira nem jött be a safari, hogy csak na, mondjuk a firefox bőven jó volt nekem :D
    Amúgy szerintem, ebben nem az a hír, hogy parázhatnak a mac userek, hanem az, hogy a "csúnya bácsik" már az almás dobozokat is csesztetni akarják ...
    meg mondjuk az emberi hülyeség és az univerzum határtalan :D (vagy csak user error )
- id: 913
  author: Rudymester
  date: '2007-11-08 08:45:20 +0100'
  date_gmt: '2007-11-07 23:45:20 +0100'
  content: |-
    Én akkor röhögtem nagyot amikor évekkel ezelőt olvastam hogy van vírus linuxra. Így kezdődött: Egy olyan autostartos cd-t kell írni...
    LOL. Az index meg egy nagy kupac barnaság,  jókat nevettem a cikkírón, amikor a Leopardot tesztelt és sokszor hivatkozott ilyen-olyan dolgokra, hogy azok mennyivel jobbak Vistán... :)
    Sohasem használtam Mac-et, de egyszerűen sületlenségeket írt a szerző. Hiába: index=fika.
---

A tűz éget. Az ég kék. Az Index FUD-ol. ([Megjelent az első trójai Macre](http://index.hu/tech/biztonsag/metm071106))

Hát persze. Legalább a Winesek nyugodtan alhatnak, hogy na hiába verik a nyálukat az újgazdag almások, az ő rendszerüket is nyugodtan zabálja vírus. Ami jelen esetben egy third-party QuickTime plug-innek álcázza magát. Ez már maga gyanúsnak kellene hogy legyen. A plug-in amúgy eredetileg korlátozott videotartalmak megtekintésére szolgál (pr0n): ez sem sikoltja, hogy szivatni akarnak, á.

Telepíteni csak úgy lehet ilyesmiket, ha a felhasználó (igen, van a "júzer"-re magyar szó, amitől az ember nem akarja letépni az arcát...) bepötyögi a jelszavát. Szóval ez kábé annyira trójai, mintha a faló ajándékba adása előtt a görögök hivatalosan is megkérdezték volna a trójaiakat, hogy elfogadják-e.

Azt is elfelejtik megemlíteni, hogy a DNS-átirányítás azért nem formatcé.

Az [Intego eredeti memoja](http://www.intego.com/news/ism0705.asp) szerint:

> After the page loads, a disk image (.dmg) file automatically downloads to the user’s Mac. If the user has checked Open “Safe” Files After Downloading in Safari’s General preferences (or similar settings in other browsers), the disk image will mount, and the installer package it contains will launch Installer. If not, and the user wishes to install this codec, they double-click the disk image to mount it, then double-click the package file, named install.pkg.
> 
> If the user then proceeds with installation, the Trojan horse installs; installation requires an administrator’s password, which grants the Trojan horse full root privileges. No video codec is installed, and if the user returns to the web site, they will simply come to the same page and receive a new download.

Aki egy kodeknek admin jelszót ad, az meg is érdemli...

A Symantec adatbázisa helyre is rakja a dolgot a "[threat assessment](http://www.symantec.com/business/security_response/writeup.jsp?docid=2007-110101-2320-99)"-jében. (Risk Level 1: Very Low)
