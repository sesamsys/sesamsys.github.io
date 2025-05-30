---
layout: post
title: kernel panic
author:
  display_name: sesam
  login: sesam
  email: petersz@me.com
  url: http://sesam.hu
date: '2012-06-14 22:23:26 +0200'
date_gmt: '2012-06-14 20:23:26 +0200'
tags:
- apple
- freeze
- iMac
- kernel
- QQ
- video
- hardware
- Tech &amp; Gizmos
comments:
- id: 8098
  author: Youkai
  date: '2012-06-15 08:21:24 +0200'
  date_gmt: '2012-06-15 06:21:24 +0200'
  content: "Részvétem, de nézd ez egyértelmű, az Apple azt szeretné, ha vennél egy
    új mac-et, nem fog azért küzdeni, hogy neked jó legyen sőt, megkockáztatom, hogy
    ez benne volt a pakliban, mint tervezett avulás. \r\nSőt ha az új MBpro-t nézem
    retinadisplay-el akkor biztos, az a gép gyakorlatilag szerelhetetlen, gondolom
    a te gépeidben is csak kb memóriát lehet cserélni. Ez a szép új világ, fogyasszál
    majd dobd el, ha meg valaki megkérdezi, hogy miért nem lehet a régit használni,
    vagy javítani akkor hülyének nézik. \r\nMondom egy 2007-es konfig mellől, amiben,
    csak az lett cserélve ami kipurcant meg kapott egy ssd-t, ebben az évben.S nem
    is tervezem jó ideig a cserét, inkább egy kis subnotit szeretnék majd Windows
    8-al :P .  Jó mondjuk ezen nincs Apple logó. De, ha azt nézzük, hogy mire használom
    a gépet, és milyen gyakran cserélem, akár lehetne is.\r\nMeglátásom szerint jobban
    járnál, ha néznél egy régebbi modellt használtan, a beszeljukmac.com-on, vagy
    várjál a nyár végégig szerintem addigra bemutatják az új Imac-ot, a régit meg
    majd jól leakciózzák."
- id: 8101
  author: SeSam
  date: '2012-06-15 12:08:00 +0200'
  date_gmt: '2012-06-15 10:08:00 +0200'
  content: Ha most valaki megdobna egy vödör pénzzel, akkor Airt vennék, meg egy szép
    nagy monitort az asztalra. :]
---

I'm sure y'all remember the [iMac freezes](http://sesam.hu/2010/11/04/24-imac-screen-freeze), I whined about them here a lot. Currently I'm running with unmodified kernel extensions because of two reasons. First, the freezes are infrequent enough to be still bearable, albeit they do come at the worst possible moments, adhering to the laws of the universe. Second, the feature introduced in Lion that resumes all running apps in the place and state they were when the shutdown was issued makes restarts much less of an issue than before.

Today I was reading an article, when... This time I wanted to do things right so I fired up the old white MacBook _"Snowflake"_ and used `ssh` to log in to the iMac, then `dmesg` to confirm that it was, in fact, the usual video freeze: for sure the kernel output had a nice long GPU dump in it. I promptly (pun intended) issued a `reboot now` command only to be greeted by this:

[![](http://sesam.hu/wp-content/uploads/2012/06/2012-06-14-22.02.08-1024x1024.jpg)](http://sesam.hu/wp-content/uploads/2012/06/2012-06-14-22.02.08.jpg)

Well, that's a first. Never before did I get a kernel panic screen.

And [Apple claims it is a hardware issue](http://sesam.hu/2012/04/07/imac-screen-freezes-caused-by-faulty-hardware).

I wonder if Mountain Lion will be any better.
