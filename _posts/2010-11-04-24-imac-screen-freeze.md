---
layout: post
title: 24&quot; iMac screen freeze
author:
  display_name: sesam
  login: sesam
  email: petersz@me.com
  url: http://sesam.hu
date: '2010-11-04 16:54:57 +0100'
date_gmt: '2010-11-04 15:54:57 +0100'
tags:
- apple
- bug
- freeze
- iMac
- osx
- QQ
- screen
- Tech &amp; Gizmos
comments:
- id: 2240
  author: Holden
  date: '2010-11-11 16:52:39 +0100'
  date_gmt: '2010-11-11 15:52:39 +0100'
  content: |-
    In my case, the only method to solve the problem was installing the smcfancontrol.
    It must be a thermal issue.
- id: 2241
  author: SeSam
  date: '2010-11-11 20:50:13 +0100'
  date_gmt: '2010-11-11 19:50:13 +0100'
  content: It cannot be a thermal issue because it is not related to GPU or CPU intensive
    applications or heavy use at all. In fact freezes often occur after the screen
    was switched off for the night or after coming back from sleep.
- id: 2242
  author: Holden
  date: '2010-11-12 05:57:35 +0100'
  date_gmt: '2010-11-12 04:57:35 +0100'
  content: |-
    I know, SESAM. I didn't run any GPU or CPU intensive apps but experienced the freezes.
    Surprisingly, after running the smcfancontrol and set about 2000 rpm, the freezes disappeared altogether.
    I was happy on 10.6.4 after that.  And I updated to 10.6.5 and uninstall the smcfanctrol. What happen? The screen freezes occurred again.
- id: 2243
  author: Kari
  date: '2010-11-12 20:17:06 +0100'
  date_gmt: '2010-11-12 19:17:06 +0100'
  content: I am having this same issue, but with 10.4.11. I have looked at the temperature
    with istat, and it is 104 degrees Fahrenheit--not enough to cause problems.
- id: 2244
  author: SeSam
  date: '2010-11-28 21:43:35 +0100'
  date_gmt: '2010-11-28 20:43:35 +0100'
  content: Tried SMCFanControl because people reported success. Fans set to 1.2k ~
    1.6k, I still got a freeze in just a few days.
- id: 2245
  author: Phil
  date: '2011-02-08 21:49:51 +0100'
  date_gmt: '2011-02-08 20:49:51 +0100'
  content: I'm current having the same problems with exact the same experiences. Did
    you have any success since then?
- id: 2246
  author: SeSam
  date: '2011-02-09 00:01:53 +0100'
  date_gmt: '2011-02-08 23:01:53 +0100'
  content: I used the workaround posted <a href="http://discussions.apple.com/message.jspa?messageID=12895464#12895464"
    rel="nofollow">here</a> by KrzysiuTurek.
- id: 3064
  author: SeSam
  date: '2011-04-20 19:07:59 +0200'
  date_gmt: '2011-04-20 17:07:59 +0200'
  content: "<strong>Update:</strong> 10.6.7 presents the same symptoms, the driver
    rollback is still unavoidable."
---

As some of the readers probably know I am a proud owner of a 2008 aluminium iMac (model 8,1).

However, lately I am being plagued by a very annoying and - so far - unavoidable issue: during use at a random point the screen just freezes, something like a permanent screenshot. I can't tell when it happens, can be weeks without it coming up at all or just after a few hours of being switched on. Sometimes the mouse still works but no input is registered. The machine usually keeps running and - for example if iTunes was on - music keeps playing in the background. I can use ssh to log in to the machine as well.

In order to put the machine out of its misery the only solution is a hard reset. (Or issuing a reboot/shutdown command from ssh.)

I can't really tell when the phenomenon started, could be around the 10.6.3 update.

I have tried the following methods so far:

  * I [switched the kernel to 64 bit mode](http://macstuff.beachdogs.org/blog/?p=134) (Leopard upgrade left me with a 32 bit default).
  * I did an [SMC](http://support.apple.com/kb/ht3964) and [PRAM](http://support.apple.com/kb/ht1379) reset.
  * I disconnected the Time Machine external HDD (connected via FireWire)



So far none of the above helped and I am getting increasingly frustrated.

Some users reported that their video card/logic board was replaced by Apple, only there is no store in Hungary and I'm out of warranty... Regardless, I can't tell if it is a software issue or a hardware issue brought up by software updates.

**Update:** So far _it seems_ that Time Machine and the Firewire drive has to do something with the freezes. Unplugged it and freezing ceased, replugged as USB and I got a lockup within the day. Doing a long-term test now with no TM/drive.

**Update 2:** I have installed 10.6.5 yesterday, replugged the TM drive and only this morning I got another freeze. Apparently the patch did nothing to fix the problem. Testing with unplugged external storage once again.

**Update 3:** OS X just got endless beachballed while no TM drive was present. Back to square one. [Apparently I'm not alone either.](http://discussions.apple.com/thread.jspa?threadID=2384136)
