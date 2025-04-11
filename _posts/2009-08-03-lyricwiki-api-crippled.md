---
layout: post
title: LyricWiki API crippled
author:
  display_name: sesam
  login: sesam
  email: petersz@me.com
  url: http://sesam.hu
date: '2009-08-03 23:13:35 +0200'
date_gmt: '2009-08-03 14:13:35 +0200'
tags:
- copyright
- harmonic
- lyrics
- lyricwiki
- MPA
- Law
- Music
comments:
- id: 2006
  author: Szak1
  date: '2009-08-04 03:05:55 +0200'
  date_gmt: '2009-08-03 18:05:55 +0200'
  content: En GimmeSomeTune-t hasznalok, jol kitoltott id3 tag eseten amikor lejatszod
    a szamot, lehuzza a szoveget es az album artot is, illetve egy gombnyomassal Growlon
    keresztul meg is jeleniti az epp jatszott szam ilyen jellegu adatait.
- id: 2007
  author: SeSam
  date: '2009-08-04 08:47:53 +0200'
  date_gmt: '2009-08-03 23:47:53 +0200'
  content: |-
    A GimmeSomeTune is használja a lyricwikit, szóval amíg ki nem adnak egy frissítést, addig azzal is belefuthatsz ebbe a problémába.

    Az albumborítókat honnan szerzi? Én azt találtam, hogy az Amazonról, ami sajnos gyakran nem éppen a legjobb minőség...
- id: 2008
  author: Mike
  date: '2009-08-04 11:27:49 +0200'
  date_gmt: '2009-08-04 02:27:49 +0200'
  content: |-
    http://lyricsfly.com/api

    Lyricwiki just signed up with the bigboys that's all. Lyricsfly doesn't seem to want to ever do that.
- id: 2009
  author: SeSam
  date: '2009-08-05 18:55:33 +0200'
  date_gmt: '2009-08-05 09:55:33 +0200'
  content: That's great Mike but what happens when their lawyers will be breathing
    down your necks?
---

Listening to Lily Allen's snarky lyrics I wanted to check the finer details so I pulled up the Dashboard to have a look at [Harmonic](http://mindquirk.com/apps/harmonic), a widget that automatically downloads song lyrics in the background for iTunes. Little did I know...

![lyricwiki-api](http://img.skitch.com/20090803-jutswx15cpkykw1fcnb5naeuhx.png)

[ Sean Colombo of LyricWiki.org explains it on the API developer page](http://groups.google.com/group/lyricwiki-api/browse_thread/thread/733ccd919d654040?pli=1):

> Dear LyricWiki API Developers,
> 
> It has been a great run, and I have seen some fantastic and interesting applications come from all of your skills and hard work.
> 
> Unfortunately, licensing agreements with the biggest publishers in the music industry require us to no longer offer the ability for programmatic access to LyricWiki's collection of lyrics. We tried to arrange some way to let API Developers license through us, but this was not possible.
> 
> While this is not something we are happy about, it is a necessity in order to finally secure licensing for LyricWiki from the major publishers which will allow the project to survive indefinitely.

Actually this is nothing new. Infuriated by their inability to stop song downloading labels decided to broaden their scope of legal threats and started to take measures against sheet music and lyrics sites: [Song sites face legal crackdown](http://news.bbc.co.uk/2/hi/entertainment/4508158.stm), reported the BBC in December, 2005.

One of the victims was [pearLyrics](http://www.pearworks.com/pages/pearLyrics.html), an automated lyrics searching application that offered a very similar service to Harmonic. The programmer of pearLyrics had to take the software down due to legal threats. [MPA](http://www.mpaonline.org.uk) president Lauren Keiser went as far as actually wanting website owners jailed:

> Mr Keiser said he did not just want to shut websites and impose fines, saying if authorities can "throw in some jail time I think we'll be a little more effective".

Now almost four years later the situation didn't seem to improve much. LyricWiki content is created entirely by users who take the time to type lyrics in from album leaflets or from listening. The site offers compensation in form of royalties to the owners that contact them. Yet in order to appease the industry even this wasn't enough.

What bothers me most in the whole story is that there is no alternative. The music industry does not offer lyrics in an electronic format. Granted CD booklets often contain lyrics but why do I have to be the one that types all that in? Not even the music downloaded from iTunes or Amazon has lyrics, even though [there is a tag that supports it](http://www.id3.org/Lyrics3v2).

I'm sure millions of lyricists died in starvation at the poorhouse because of Harmonic and lyricWiki.

Now I'm wondering if it would be possible to use the API to identify the lyrics URL then have curl grab the page and apply some regexp to extract the valuable part (the lyrics). Not that I could code it, but I recall a last.fm stalking script that created a growl notification from a person's "listening now" status working quite the same way.
