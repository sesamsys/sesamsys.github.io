---
layout: post
title: eXPerience
author:
  display_name: sesam
  login: sesam
  email: petersz@me.com
  url: http://sesam.hu
date: '2007-01-28 01:55:06 +0100'
date_gmt: '2007-01-27 16:55:06 +0100'
tags:
- Tech &amp; Gizmos
comments: []
---

Ugye már volt róla szó, hogy még [anno szerettem volna XP-t](http://sesam.hu/2006/12/07/ntldr) az asztali gépre a játékoknak. Akkor felhagytam az ötlettel, legalábbis addig, amíg meg nem jelenik a végleges Vista. Egészen röviden ugye arról volt szó, hogy vagy el se indult az installer (fekete képernyő) vagy ha be is töltötte magát nem detektálta rendesen a partíciókat. Lévén nem nyúlhattam hozzá a már meglévő partíciókhoz, hiszen azokon leledzett a gentoo, annyiban is maradt a dolog.

Most tettem egy próbát a Campusos SP2 telepítővel és bár elsőre ugyanúgy elfeketedett örökre mint az eredeti telepítőm másodjára furamód elindult, mi több meg is látta a partíciókat rendesen. Úgy fest a szintén [korábban részletezett NTFS-korlát](http://sesam.hu/2007/01/19/fs-stowies) a probléma, azaz hogy az XP eredetileg nem ismer nagyobb HDD-t, mint 13xG.

Lényeg ami lényeg feltelepült, kattintanék az explorerre de közli, hogy nincs net. Persze nForce alaplapi LAN-t nem ismeri a Win, hiába SP2, úgyhogy elő kellett halásznom az alaplaphoz adott CD-t. Ami úgy mellesleg Cool'n'Quiet, AC97, stb. drivereket is felpakolt. Na rebootkor jött a meglepetés: hirtelen lett boot menü két választással "Windows" és "Microsoft Windows XP Professional Edition", melyek közül az előbbi valami csúf rendszerhibával azonnali elszállást produkált, az utóbbi pedig a load-képernyő változatos pontjain halt le. De annyira, hogy kezdhettem előről az egészet. Nem tudom, hogy az nVidia vagy az alaplapgyártó GigaByte felelős-e ezért a gyöngyszemért, de igen jól sikerült megírni azokat a drivereket... Valamivel nagyon mellényúltak, mert ilyen kék képernyőket még eddigi Wines pályafutásom alatt nem láttam.

Harmadik telepítés után próbáltam azt, hogy csak az nForce chipset drivert tettem fel, ami szerencsére nem produkálta a fenti gondokat viszont életre lehelte a LAN-t, és lett netem. Ezután viszonylag eseménytelen volt a [ForceWare](http://nvidia.com) > [Firefox](http://www.getfirefox.com) > [AVG](http://free.grisoft.com) > [Java](http://java.com/en/download/index.jsp) > [Azureus](http://azureus.sourceforge.net) > [Anarchy Online](http://www.anarchy-online.com) sorrend. A Win kifejezetten stabil, ha csak AO-zásra használják.

Persze MBR szépen felül lett írva, és a 4. partícióról bootolt a gép (értsd: amelyiken a Win van). Eljött az idő ezt rendbeszedni, és visszahozni a Gentoot. LiveCD, chroot, grub install. Ha ez ilyen egyszerű lenne... ugyanis a LiveCD valamiért máshogy szedte sorba a vinyókat (2 SATA és 2 ATA) (hd0,0)-ból (hd2,0)-t generálva, ami azért eltartott egy darabig míg világossá vált számomra. Innentől persze sima ügy, és lőn dualboot.

Persze nem tökéletes, mert reboot kell ha játszhatnékom van, de azért csak 40fps és 19"... :)
