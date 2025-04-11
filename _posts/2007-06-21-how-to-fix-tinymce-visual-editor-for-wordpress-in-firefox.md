---
layout: post
title: How to fix TinyMCE (visual editor) for WordPress in Firefox
author:
  display_name: sesam
  login: sesam
  email: petersz@me.com
  url: http://sesam.hu
date: '2007-06-21 13:21:35 +0200'
date_gmt: '2007-06-21 04:21:35 +0200'
tags:
- Tech &amp; Gizmos
comments: []
---

For starters, I have upgraded the site to [WP 2.2](http://wordpress.org/download) from 2.0.5. The usual favour applies: if something doesn't seem to function, please do [contact](http://sesam.hu/contact) me.

One reason of the upgrade was that I hoped for the visual editor to somehow "un-bug" itself and actually work. However, it didn't happen. Searching for the reason resulted in a lot of complaints from people using Firefox, meanwhile everyone claimed it worked flawlessly under IE. That's when I thought of [AdBlock Plus](http://adblockplus.org/en)... the usual reason behind stuff mysteriously breaking in websites, also one of the most widely used Firefox plug-ins. And boy was I right. Some of the visual editor's (a.k.a. TinyMCE) scripts were caught in ABP's filters.

As a quick fix simply add the following exception to your ABP rules:

@@http://<path-to-WordPress>/wp-includes/js/tinymce/

And that's it, full featured visual editor welcomes you after refresh.

Two features that I instantly loved: tabbed editor, one for Visual and one for Code, for those who like to hack even more formatting in their posts. (Like the different styling of the code above.) And regular automatic save of the posts. (Raise your hand if you bothered saving every now and then, just to be safe. Raise your other hand if you've ever lost a post by some stupid mistake, like hitting reload accidentally. Okay, you can put your hands down. Those days are over.)
