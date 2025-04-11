---
layout: post
title: do a lil bit of scrobbling
author:
  display_name: sesam
  login: sesam
  email: petersz@me.com
  url: http://sesam.hu
date: '2007-09-07 02:17:50 +0200'
date_gmt: '2007-09-06 17:17:50 +0200'
tags:
- Music
- Tech &amp; Gizmos
comments:
- id: 805
  author: Vale
  date: '2007-09-07 04:41:36 +0200'
  date_gmt: '2007-09-06 19:41:36 +0200'
  content: i suppose another $ret[$i]['artist-url'] should be there soon after. i'll
    check this one out if i have some free time, i like diving into long complicated
    scripts.
- id: 806
  author: Stefan Ernst
  date: '2007-09-11 04:41:21 +0200'
  date_gmt: '2007-09-10 19:41:21 +0200'
  content: Now we'll just need that same thing for Typo3. ;)
---

Eagle-eyed readers might have noticed that the now playing ticker now changed to display last.fm links as well. I really would have switched this option on earlier, but the artist link was bugged in the latest [scrobbler add-on for WP](http://leflo.de/projects/scrobbler).

Turned out the "bug" was really just a minor issue and took [sld](http://sld.interhost.hu/sld) about 30 seconds to fix. Here's what you should change in your phpScrobbler.php file, provided that you're using version 2.2.7 of the add-on:

`$ret[$i]['artist-url'] = "http://www.last.fm/explore/search.php?q=";`  
should be  
`$ret[$i]['artist-url'] = "http://www.last.fm/music/";`  
and just comment out the following line  
`// $ret[$i]['artist-url'] .= "&m=artists";`

Violá, bug fixed, %artist-url% now displays the correct link when used on the configuration panel.
