---
layout: post
title: Force Unicode (UTF-8) reply in Mail.app on OS X Mountain Lion
author:
  display_name: sesam
  login: sesam
  email: petersz@me.com
  url: http://sesam.hu
date: '2013-07-19 17:06:11 +0200'
date_gmt: '2013-07-19 15:06:11 +0200'
tags:
- encoding
- OS X
- Japan
- Mountain Lion
- Mail
- UTF-8
- Tech &amp; Gizmos
comments: []
---

Heuréka! Elképesztően sokat szívtam azzal, hogy az OS X Mail alkalmazásában nem lehet alapértelmezett kódlapot beállítani, de most megvan a megoldás.

A munkámból adódóan sokat írnak nekem japánok, akiknek sajnos az a rossz szokásuk, hogy ISO-2022-JP enkódolásban küldik a leveleiket. Ezeket persze a Mail.app minden gond nélkül megjeleníti. Azonban ha egy ilyen levelet továbbítok, vagy válaszolok rá, akkor megmarad a japán kódlap. Ez még mindig nem lenne baj, mert a Mail.app van olyan intelligens, hogy helyesen mutatja az emailt, viszont mindenki más, aki mondjuk a Gmail webes felületén nézi, olvashatatlan karakterláncot lát csak. Így a dolognak még az a szépsége is megvan, hogy csak akkor értesülök a fiaskóról, amikor valaki megmutatja, hogy mit küldtem neki.

Az egyik megoldás, hogy minden egyes alkalommal, amikor ilyen emailre válaszolok, átállítom a kimenő levél enkódolását a Message > Text Encoding > Unicode (UTF-8) menüvel. A módszer hátulütője, hogy macerás minden elküldendő emailnél végigkattintani, illetve hajlamos vagyok elfelejteni. Fixen beállítani természetesen nem lehet.

Az internet tele van a második opcióval, hogy a terminálból adjuk ki a `defaults write com.apple.mail NSPreferredMailCharset "UTF-8"` parancsot. Ez azonban Leopard óta megszűnt működni, tehát kuka.

Ami viszont bizonyítottan **működő megoldás, ha egy[Dingbat](http://en.wikipedia.org/wiki/Dingbat) karaktert helyez el az ember az emailben**, esetemben például az aláírásban. Ha ilyen karakter van az email szövegében a Mail.app automatikusan Unicode kódolással küldi el, mindegy, milyen karakterlapú emailre válaszolunk.

Nem egy esztétikus hack, de működik.
