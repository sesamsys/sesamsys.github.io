---
layout: post
title: Adium EVE icon
author:
  display_name: sesam
  login: sesam
  email: petersz@me.com
  url: http://sesam.hu
date: '2009-03-09 00:15:06 +0100'
date_gmt: '2009-03-08 15:15:06 +0100'
tags:
- Adium
- dock
- EVE
- icon
- osx
- Pixar
- Wall-E
- fun
- Movies &amp; TV
- Tech &amp; Gizmos
comments: []
---

Besides being the cutest thing ever [EVE](http://www.imdb.com/character/ch0089609) (short for Extra-terrestrial Vegetation Evaluator) is said to be influenced by the latest Mac designs. So it is only appropriate if she appears on the Dock, which is exactly what this EVE icon set for Adium [by mxmln](http://mxmln.blogspot.com/2008/04/wall-e-eve-adium-icon.html) offers:

[![EVE-Adium](http://img.skitch.com/20090308-ft5rnw6s7wqduuk139ugjt4dpf.png)](http://www.adiumxtras.com/index.php?a=xtras&xtra_id=5446)

Disconnected she is in "plant mode" and upon message reception she gets the smiley eyes. My only woe is that there is no indication whatsoever for the away status. Nevertheless this is a minor issue compared to the sheer awesomeness of the whole thing. [Download it here.](http://www.adiumxtras.com/index.php?a=xtras&xtra_id=5446)

What bothers me more is this Adium bug: the dock icon keeps reverting to the default green bird when I quit. I've tried everything: restarted the dock, removed and reapplied the icon, reinstalled Adium, to no avail. [I opened a ticket on in the trac system](http://trac.adiumx.com/ticket/11760), but until now it's been pretty quiet.

**Update:** I managed to fix the icon! Apparently I used the wrong approach to remove and re-add. Removing then using Spotlight to start the program then pulling the icon to place would not work. I had to remove the icon then _pull the app bundle from the Applications folder to the Dock_ to fix. Hope this helps.
