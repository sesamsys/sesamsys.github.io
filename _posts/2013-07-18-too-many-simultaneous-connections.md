---
layout: post
title: Too many simultaneous connections
author:
  display_name: sesam
  login: sesam
  email: petersz@me.com
  url: http://sesam.hu
date: '2013-07-18 13:00:07 +0200'
date_gmt: '2013-07-18 11:00:07 +0200'
tags:
- OS X
- GMail
- Mail
- Tech &amp; Gizmos
comments: []
---

Ma [kiírtam Twitterre](https://twitter.com/sesam/status/357799438472847362) egy parancsot, amivel kilépésre lehet bírni bármilyen OS X alkalmazást parancssorból. A fene gondolta, de nagyon népszerű lett.

A háttér, hogy a céges emailünk Google Apps alapú, amit én minden gépemen Mail.app-ban nézek. Gyakran előfordul, hogy az otthoni gépen is bekapcsolva marad a Mail.app. Ez azért lehet gond, mert ha túl sok kérés esik be a Gmailhez, (konkrétan több, mint 15 IMAP kapcsolat fiókonként) akkor [Too many simultaneous connections](https://support.google.com/mail/answer/97150?hl=en) hibát dob. Egy kliens pedig a háttérben több kapcsolatot is nyithat.

Igény van rá tehát, hogy a munkahelyről ki lehessen lépni az otthoni Mail.app-ból. Ehhez szükség van ssh elérésre, amit simán be lehet kapcsolni az OS X beállításaiban, egy port átirányításra az otthoni routerben, és az otthoni IP címre, amit én a [Dyn](http://dyn.com/dns) ingyenes DNS szolgáltatásával kötöttem össze.

Ha már bent vagyunk, elég lenne egy sima kill parancsot kiadni, de az nem túl elegáns. Sokkal szebb az:

`osascript -e 'tell application "Mail" to quit'`
