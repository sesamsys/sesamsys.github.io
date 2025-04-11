---
layout: post
title: FS stowies
author:
  display_name: sesam
  login: sesam
  email: petersz@me.com
  url: http://sesam.hu
date: '2007-01-19 13:53:30 +0100'
date_gmt: '2007-01-19 04:53:30 +0100'
tags:
- Tech &amp; Gizmos
comments: []
---

(Caveat: nem tudom eldönteni, hogy erről írtam-e már vagy csak akartam...) Még régebben történt, hogy apa kért egy nagyobb winchestert a munkahelyi gépébe. AMikor visszakapta a 120GB helyett, amekkorát eredetileg szeretett volna, egy 20GB-os lapult benne, azzal az indokkal, hogy a régi Win98-as gépe nem kezeli a 32GB-nál nagyobb merevlemezeket. Én kissé furcsállottam a dolgot, emlékeim szerint a FAT32-nek ennél nagyobb területet illene azért kezelnie. A válasz a [FAT](http://en.wikipedia.org/wiki/File_Allocation_Table) wiki oldalában rejlett, mely szerint a Microsoft szándékosan limitálta a Windowsok particionáló programját. Magyarázattal nem szolgál, hacsak azzal nem, hogy a filerendszer egyszerűségéből adódóan durva teljesítményzuhanást okoz a nagy területek kezelése.

Persze senki sem akar FAT-ot használni ha van NTFS (mondja a Microsoft) de - mint a fenti példából is látható - előfordulhatnak kompatibilitási problémák, amikoris jó lenne azért. Ha valaki egy normális programmal csinál egy 32GB+ FAT32 partíciót, a Win látja ugyan, de itt viszont a 95/98 lemezkezelő segédprogramjai szólnak bele a limitbe. Tekintve, hogy ezek (Scandisk és társai) 16 bites programok, a FAT32 partíció mérete nem lehet 127GB-nál több.

Éz a probléma visszaköszön ám az NTFS-el is. Tesó ballagási számítógépére kellett volna XP-t pakolni, mikor az installer szépen közölte, hogy a 160GB-os vinyó csak 120 körüli. A [Seagate](http://www.seagate.com/ww/v/index.jsp?vgnextoid=6bd0781e73d5d010VgnVCM100000dd04090aRCRD&locale=en-US) oldalán van egy FAQ erről: a pre-SP XP-k beépített limittel rendelkeznek NTFS esetén is. Természetesen ha valaki vett egy XP-t, nem kap új telepítőt a frissítések után. (Miénk Campus-os, lehet letölteni újat.) Így elméletileg a megoldás az lenne, hogy egy kisebb partícióra feltéve az XP-t frissíteni SP2-re (SP1 is elég), majd egy külső programmal kiterjeszteni a partíciót az egész winchesterre. Természetesen ezeket a szoftvereket a legritkább esetben adják ingyen.

Mi inkább fogtunk egy Knoppix CD-t, (Ami egy teljesértékű CD-ről futó KDE-t varázsol mellesleg a gépre pillanatok alatt.) és linuxos fdisk-el partícionáltunk. A win installere a partíciókat már helyesen látta, de persze a HDD mérete maradt 127GB.

Itt a tendencia tehát, hogy - meglehetősen dokumentálatlanul - mindenféle limitálások vannak beépítve a winekbe, melyek egyszer csak kiderülnek, nem kevés bosszúságot okozva.

Összehasonlításul az OS X filerendszere ([HFS+](http://en.wikipedia.org/wiki/HFS%2B)) technológiai mérethatára 32EiB, amely azonban limitált az egyes operációs rendszer verziók esetén: Mac OS 8 (1997) 2TiB, OS X 10.3 (2003) 16TiB. Ehhez képest tud a 2001-ben kijött XP annyit amennyit... (32G, 127G)

Linuxról inkább nem is mondok semmit: Ferrari-Trabant az arány.

Valószínű egy átlagfelhasználó fejében a következőképp értelmeződik a probléma: "Hű, a 160GB-os vinyómat nem látja a számítógép! Vennem kell egy új gépet/alaplapot!" Aztán mikor megtudja, hogy a Vista telepítője bizony látja a megfelelő méretet ismét levonja a konklúziót. Az mondjuk feltűnő lehetne, hogy a Vista is ugyanarra a (v3.1) NTFS-re formáz...
