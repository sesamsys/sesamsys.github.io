---
layout: post
title: iMac screen freezes caused by faulty hardware
author:
  display_name: sesam
  login: sesam
  email: petersz@me.com
  url: http://sesam.hu
date: '2012-04-07 11:09:16 +0200'
date_gmt: '2012-04-07 09:09:16 +0200'
tags:
- apple
- freeze
- iMac
- QQ
- screen
- support
- warranty
- Tech &amp; Gizmos
comments:
- id: 7398
  author: Youkai
  date: '2012-04-10 11:56:49 +0200'
  date_gmt: '2012-04-10 09:56:49 +0200'
  content: "Auch.... :S\r\nPróbáltad már, hogy linux vagy windows alatt is csinálja
    e- ezt a géped ?\r\nAmúgy meg felhívnám az idokit, ezért is \r\n\r\n\"..iBook,
    PowerBook, iMac G4, G5 kijelzőhiba (GPU, videókártya, csíkos, sávos, foltos, szétesett
    kép) javítása 20.000 Ft. \r\nMacBook, MacBook Pro, iMac Intel kijelzőhiba (GPU,
    videókártya, csíkos, sávos, foltos, szétesett kép) javítása 40.000 Ft. \r\nCinema
    Display táp javítás: 30.000 Ft...\" egy telefont megér... \r\n\r\n40k meg egy
    vga cseréért egy mac-ba szerintem nem drága, nekem 34k volt amikor a pc-ben elfüstölt
    a 8800 GTS, jó, mondjuk azt kb 5 perc alatt megszereltem :P"
- id: 7501
  author: John Miller
  date: '2012-04-18 04:50:13 +0200'
  date_gmt: '2012-04-18 02:50:13 +0200'
  content: "Thanks for sharing.  Same thing is happening to my iMAC which is of the
    same 2008 vintage and has been freezing every couple days -likely since one of
    the new releases.  If the root cause is what they tell you it is, Apple should
    provide a patch that disables the code that exploits this problem.  It should
    be their responsibility if they produced a run of iMACs all with faulty hardware
    that only now is showing up because of video driver problems.\r\n\r\nLet us know
    if you have any more success, and I'll need to find out how to back out these
    kernel extensions.\r\n\r\nJohn Miller\r\nCanada"
- id: 7563
  author: bat
  date: '2012-04-23 07:10:30 +0200'
  date_gmt: '2012-04-23 05:10:30 +0200'
  content: MO-n melyik szerviznel sikerult elerni ezt az attorest? nekem 2 gepem van,
    de nem nagyon aktivizaljak magukat...
- id: 7564
  author: SeSam
  date: '2012-04-23 07:59:34 +0200'
  date_gmt: '2012-04-23 05:59:34 +0200'
  content: Nincs szó magyar szervízről az írásban. Nem voltam még egyiknél sem soha.
- id: 7565
  author: bat
  date: '2012-04-23 09:29:10 +0200'
  date_gmt: '2012-04-23 07:29:10 +0200'
  content: akkor közvetlenül apple-hez fordulni (Tim Cook) a recept?
- id: 7571
  author: SeSam
  date: '2012-04-23 22:06:10 +0200'
  date_gmt: '2012-04-23 20:06:10 +0200'
  content: 'Ismét csak nem: azon kívül, hogy megállapították a hardverhibát, semmi
    sem történt. Ha van garanciád, akkor szerencséd van, ha nincs, így jártál.'
---

The title basically spoils the ending, but here's how my dealings with Apple went regarding the freezing iMac.

To recap the issue: ever since 10.6.3 some [Macs produce video freezes](http://sesam.hu/2010/11/04/24-imac-screen-freeze) where the computer remains running but cannot be interacted with. Screen can black out, white out, show stripes or just an endless beachball. The only solution is to hard reset or - occasionally - use ssh to log into the machine and issue a reboot command. The kernel.log is usually flooded with a particularly disgusting GPU dump.

There is a fairly extensive discussion about this problem on the Apple Support Communities board which **started in March 2010** : _[24" iMac Screen Freezes since 10.6.3 update - pls help!](https://discussions.apple.com/thread/2384136?tstart=0)_

People in the thread determined that something in the video drivers cause the freezes and that **the relevant kernel extensions can be swapped to their 10.6.2 counterparts** which stops the lockups. Of course one loses two years worth of video driver updates this way. Regardless, I've been doing this for every OS X update since then.

Feeling that I exhausted all available options one day in February I was just fed up enough to exasperatedly email Tim Cook. After all some people did get a reply...

To my huge surprise I did actually receive a response from an Executive Relations representative who forwarded the issue to a Senior Apple Care Specialist. Although the warranty on the iMac has long been expired, they agreed to deal with the case based on the assumption that it is a software problem. I was quite hopeful we could finally find out the cause of this issue together.

Over the phone I was instructed to set up a separate partition with a fresh install of OS X Lion to prove that none of my installed third party software are the culprit. For weeks I was trying to reproduce the freeze on that installation with little success almost losing belief that it would occur until finally it did freeze out on me, classic rainbow cursor style. Logs and system information were gathered and sent over in hope.

Only the reply I got a week later was a major letdown: **the engineers allegedly determined that the root of the issue is malfunctioning hardware**. I was told that since the warranty had expired they are unable to offer a replacement video card or any other free solution. What's infuriating about this is that my iMac is an early 2008 model; 10.6.3 came out on 29 March 2010, meaning **I was most likely out of the 1 year warranty when I even had the chance to find out about the problem**. Along with several others I was sold a computer with allegedly faulty hardware, with said fault well hidden during the time covered by warranty. That, or everyone's video cards just fried the day 10.6.3 came out...

I seem to recall that replacement programs have been started for much less. Also we are talking about a company with enough cash to buy my home country's national debt. And I still get to use a computer with a broken video card.
