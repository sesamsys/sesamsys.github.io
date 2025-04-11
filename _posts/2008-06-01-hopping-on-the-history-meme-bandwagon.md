---
layout: post
title: Hopping on the history meme bandwagon
author:
  display_name: sesam
  login: sesam
  email: petersz@me.com
  url: http://sesam.hu
date: '2008-06-01 11:14:49 +0200'
date_gmt: '2008-06-01 02:14:49 +0200'
tags:
- history
- linux
- meme
- fun
- Tech &amp; Gizmos
comments:
- id: 1324
  author: Vale
  date: '2008-06-01 17:17:56 +0200'
  date_gmt: '2008-06-01 08:17:56 +0200'
  content: bár működne a linuxom...
- id: 1325
  author: Ardin
  date: '2008-06-02 18:39:30 +0200'
  date_gmt: '2008-06-02 09:39:30 +0200'
  content: Bár érteném, mi ez... :D
- id: 1326
  author: SeSam
  date: '2008-06-02 18:42:34 +0200'
  date_gmt: '2008-06-02 09:42:34 +0200'
  content: Gyakorlatilag egy statisztika arról, hogy milyen parancsokat használsz
    a legtöbbször. Ha hozzá tudsz férni valamilyen *nix géphez, próbáld ki a history
    parancsot. :)
- id: 1327
  author: SeSam
  date: '2008-06-02 18:48:40 +0200'
  date_gmt: '2008-06-02 09:48:40 +0200'
  content: Az <em>mplayer</em> elég egyértelmű, a <em>startx</em>-el indítom a grafikus
    felületet (nem használok garfikus logint), a <em>su</em> jelentése switch user,
    és root felhasználóba válthatok vele. A <em>cd</em> a DOS cd parancssal egyenértékű.
    Az <em>mc</em> a Midnight Commander, egy Norton Commander klón. Az <em>ls</em>
    a DOS dir parancsához hasonlóan működik. Az <em>sshfs</em> egy speciális program,
    amivel ssh-n keresztül lehet távoli filerendszereket elérni a hálózaton (én a
    MacBook vinyóját nézegetem vele).  A <em>screen</em> kicsit bonyolult, gyakorlatilag
    egy konzolablakból csinál többet. A <em>df</em>-el a merevlemez kihasználtságát
    lehet listázni, és végül az <em>rm</em> a törlés parancsa. :)
- id: 1328
  author: Ardin
  date: '2008-06-02 21:23:06 +0200'
  date_gmt: '2008-06-02 12:23:06 +0200'
  content: Köszönöm a felhomályosítást ;)
---

`sesam@lillemor ~ $ uname -a  
Linux lillemor 2.6.24-gentoo-r4 #1 SMP Tue Apr 8 12:07:37 JST 2008 x86_64 AMD Athlon(tm) 64 X2 Dual Core Processor 4200+ AuthenticAMD GNU/Linux  
sesam@lillemor ~ $ history | awk '{a[$2]++}END{for(i in a){print a[i] " " i}}' | sort -rn | head  
128 mplayer  
49 startx  
48 su  
31 cd  
30 mc  
29 ls  
17 sshfs  
15 screen  
14 df  
11 rm`
