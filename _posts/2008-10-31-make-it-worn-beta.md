---
layout: post
title: Make It Worn beta
author:
  display_name: sesam
  login: sesam
  email: petersz@me.com
  url: http://sesam.hu
date: '2008-10-31 16:59:03 +0100'
date_gmt: '2008-10-31 07:59:03 +0100'
tags:
- design
- template
- wordpress
- Tech &amp; Gizmos
comments:
- id: 1534
  author: Stefan Ernst
  date: '2008-10-31 20:34:08 +0100'
  date_gmt: '2008-10-31 11:34:08 +0100'
  content: This is a lot nicer than the old design. =)
- id: 1535
  author: SeSam
  date: '2008-10-31 21:01:18 +0100'
  date_gmt: '2008-10-31 12:01:18 +0100'
  content: Thank you. The old one had the years pass over it really... and this one
    was actually done by someone who've seen Photoshop before. :P
- id: 1536
  author: Stefan Ernst
  date: '2008-11-02 21:47:41 +0100'
  date_gmt: '2008-11-02 12:47:41 +0100'
  content: And I'm rather inspired by that for evolving the pvc site some more into
    the grunge/worn look which I was always wanting to do. &gt;.&lt;
---

It's been a while I stumbled upon [Bart-Jan Verhoef](http://subdued.net)'s site and his [three-part tutorial on how to create a worn look to a site](http://www.subdued.net/make-it-worn). He was kind enough to share a template page to show how he built up the final design. I liked it instantly and decided to implement it for WordPress.

You may remember I have been dissatisfied with how the journal was designed for a while now. I wanted something cleaner, wider, more serious and less emo. Bart-Jan's worn look is just like that with the additional perk of keeping the aged papery texture of my old clumsy design. So here's how SeSam.hu will look from now on.

I was trying to be as faithful to the original template page as possible. However WordPress has some specialities and it needs to integrate a wider array of functions which made it necessary to move a few pixels around. (The IE bug that prevents elements from floating properly in rows is a prime example. That one took hours to fix and caused a significant headache.)

I have to admit, building a template for WordPress is not an easy job. Unlike when I was just designing for myself a proper distributable template needs to be a lot more flexible and adapt to all the different blogs out there. The design must be prepared to handle a plethora of data structures. It remains to be seen how well I did to achieve that.

Not all the features I wanted are included, but I felt the design was ready for a live beta. Please if you encounter any quirks, malfunctions or errors do [contact me](http://sesam.hu/contact) or comment to this post.

Features or functions missing that I'd like to implement:

  * There's no indication when you're browsing the archives of where you actually are. As in "You're browsing the archives for August 2006." or so. Search results lack likewise.
  * I'd like a search form on the index page, but not sure yet where to put it.
  * Blockquotes should get a nicer design not just an indent.
  * The 404 page is missing.
  * At least the single post pages should show the categories and tags. I found that there are too many of them to fit in the little "entry details" field and when I tried it broke the grid layout.
  * I should add some more usability enhancements such as indicating required fields when commenting, listing the usable bbcode, links to trackbacks and pingbacks...
  * Code needs cleaning for validity, something I haven't yet checked.



Features unlikely to be implemented:

  * The design is theoretically a three-column one, nevertheless there's not enough space for sidebars, so there are none. A possible rework of the entire index page might introduce them...
  * I am not really familiar with the process of making a template open to language packs, therefore that feature is missing.
  * Having too many pages will surely break the header. The template is ill-suited to such sites.



I'm sure as soon as I press publish a dozen more will spring to my mind.

Anyway, if you like it and would like to use it I ask only a little bit of your patience just yet. Before making a downloadable version I'd like to sort a few things out and add the missing features. The reason why I applied it to SeSam.hu is that I'd like to test it live. Naturally since the whole site is licensed under creative commons if you insist on having this beta version [email me](http://sesam.hu/contact) and I shall send it to you.
