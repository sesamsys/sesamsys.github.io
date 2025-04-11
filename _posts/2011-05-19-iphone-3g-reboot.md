---
layout: post
title: iPhone 3G reboot
author:
  display_name: sesam
  login: sesam
  email: petersz@me.com
  url: http://sesam.hu
date: '2011-05-19 15:28:18 +0200'
date_gmt: '2011-05-19 13:28:18 +0200'
tags:
- iphone
- iOS
- push
- jailbreak
- carrier unlock
- ultrasn0w
- 3G
- 4.2.1
- Tech &amp; Gizmos
comments: []
---

People who know me or at least follow me on [Twitter](http://twitter.com/#!/sesam) know that I've been plagued by a nasty bug with the hacked iPhone software since I started using iOS 4.1. During normal daily use the phone would flicker feebly then reboot for no reason whatsoever. To make matters worse in these cases the OS loaded several minutes slower than a normal boot would.

A few days ago finally decided I've had enough. As the first step I tried to re-jailbreak the phone and reinstall 4.1 from DFU mode. After restoring from the backup - even though the firmware felt much snappier - the problem surfaced again. Next I tried omitting the backup entirely and set up a new phone. No luck, the following day I had a random reboot again.

Then I realized (the blog post must have slipped my attention) that there actually exists [a version of Pwnage tool that installs 4.2.1 without modifying the baseband](http://blog.iphone-dev.org/post/3314130778/whats-in-a-name). This is important because the ultrasn0w carrier unlock only works on specific baseband versions which are usually updated when new iOS versions are released.

So I updated to 4.2.1, set up as new, and finally I got a stable phone. Only there was a nagging issue: push notifications stopped working. Even though I've had enough life lessons about _'if it's not broken, don't try to fix it'_ , I set out to get push back.

One offered solution is [Subscriber Artificial Module (SAM)](http://www.bingner.com/SAM.html), a piece of software that spoofs a fake SIM to iTunes and lets you activate as if you had the correct carrier's SIM. Only it would have been too easy if it worked: I couldn't find a single option that was accepted by iTunes as a Softbank SIM.

Then it occurred to me, why can't I just restore from backup with the 4.2.1 software? After all it was - seemingly - the firmware that caused the restarts, it had nothing to do with the backup, and also I did have push before - even on 4.1 - probably as a remainder from the legitimate Softbank activation. So after several cumulative hours of flashing, organizing apps and synchronizing now I have an **iPhone 3G** that runs **4.2.1** with active **push** and no random reboots.

I could have done this sooner. Partly I was lazy to do the whole boring process of updating again and again and I was afraid I'd lose the only phone I have and can afford. Turns out I could have been more optimistic and self-assured: _if I want something bad enough, keep on trying no matter how much time it needs to be done, and never give up... then it might just happen_.
