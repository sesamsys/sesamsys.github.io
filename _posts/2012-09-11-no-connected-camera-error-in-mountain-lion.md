---
layout: post
title: No Connected Camera Error in Mountain Lion
author:
  display_name: sesam
  login: sesam
  email: petersz@me.com
  url: http://sesam.hu
date: '2012-09-11 10:31:19 +0200'
date_gmt: '2012-09-11 08:31:19 +0200'
tags:
- bug
- OS X
- Mountain Lion
- camera
- Tech &amp; Gizmos
comments: []
---

Quite annoyingly after the computer goes to sleep and wakes up again, some applications have trouble recognising the built-in camera. Up until now I resorted to rebooting the Air, which is not that a big deal when you have an SSD, but still I wished I didn't have to. [Turns out](https://discussions.apple.com/thread/4158054) there is an easier solution: an application called **VDCAssistant** is reserving the camera in these cases, which is safe to be killed either from the Activity Monitor or by issuing:

`sudo killall VDCAssistant`
