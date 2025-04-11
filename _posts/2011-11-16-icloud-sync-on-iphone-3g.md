---
layout: post
title: iCloud sync on iPhone 3G
author:
  display_name: sesam
  login: sesam
  email: petersz@me.com
  url: http://sesam.hu
date: '2011-11-16 10:26:59 +0100'
date_gmt: '2011-11-16 09:26:59 +0100'
tags:
- Android
- apple
- iphone
- MobileMe
- iOS
- iCloud
- Tech &amp; Gizmos
comments: []
---

Bár az [iOS 5](http://www.apple.com/ios) nem kompatibilis az eredeti iPhone-nal és az iPhone 3G-vel, az új [iCloud](http://www.apple.com/icloud) szinkronizációs rendszer email, naptár és kontaktlista szolgáltatása ugyanúgy használható kézi beállítással. Sőt, bármilyen **IMAP** , **CalDav** és **CardDav** protokollt támogató szoftverrel együttműködik: nekem az Androidon is sikerült iCloud emailt csiholnom.

iOS alatt a `Settings > Mail, Contacts, Calendar > Add Account… > Other` menüben lehet beállítani mindhárom szolgáltatást.

A szükséges adatok a következők:

  * Bejövő IMAP szerver: `imap.mail.me.com`
  * Kimenő SMTP szerver: `smtp.mail.me.com`
  * Naptár szerver: `caldav.icloud.com`
  * Kontakt szerver: `contacts.icloud.com`
  * Felhasználónév: `az iCloud email cím`



A [neten fellelhető leírásokban](http://wyctim.com/icloud-sync-regebbi-rendszereken) említett `p01-p03` prefixekre saját tapasztalatom alapján nincs szükség, ezt az iOS automatikusan kitölti a szerver ellenőrzése közben.

Fontos viszont odafigyelni, hogy **ha valakinek a régi`@mac.com` email címe is él, akkor azt írja be felhasználónévnek**. Nekem mind a naptár mind a kontaktlista szinkronizáció csak így működött, a `@me.com` végű címmel nem.
