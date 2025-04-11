---
layout: post
title: Analytics plugin bug
author:
  display_name: sesam
  login: sesam
  email: petersz@me.com
  url: http://sesam.hu
date: '2008-12-19 08:57:13 +0100'
date_gmt: '2008-12-18 23:57:13 +0100'
tags:
- Analytics
- bug
- fix
- google
- wordpress
- Tech &amp; Gizmos
comments:
- id: 1701
  author: Mica bug al plugin-ului Google Analytics (Rich Boakes)
  date: '2008-12-21 05:17:28 +0100'
  date_gmt: '2008-12-20 20:17:28 +0100'
  content: "[...] Daca va uitati mai bine e vorba doar de un semnul intrebarii. Care
    semnul intrebarii mi-a pus si mie cateva semne de intrebare pana am dat de asta.
    [...]"
---

You may have noticed a recent issue with comment author links: they had '%20rel='external%20nofollow" appended to the end of the URL. Apparently this is an incompatibility bug with the [Google Analytics plugin by Rich Boakes](http://boakes.org/analytics) (v0.68) and the latest release of WP. [I found a thread on the WP support forums detailing a fix which I'm happy to say works.](http://wordpress.org/support/topic/224480) Simply change the following line in googleanalytics.php:
    
    
    function comment_author_link($text) {
    	static $anchorPattern = '(.*href\s*=\s*)[\"\']*(.*)[\"\'] (.*)';

To this:
    
    
    function comment_author_link($text) {
    	static $anchorPattern = '(.*href\s*=\s*)[\"\']*(.*\?)[\"\'] (.*)';

Gotta love regexp. :)
