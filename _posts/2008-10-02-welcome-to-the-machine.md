---
layout: post
title: Welcome to the Machine
author:
  display_name: sesam
  login: sesam
  email: petersz@me.com
  url: http://sesam.hu
date: '2008-10-02 23:24:27 +0200'
date_gmt: '2008-10-02 14:24:27 +0200'
tags:
- QQ
- TinyMCE
- valid code
- wordpress
- Tech &amp; Gizmos
comments: []
---

So I was frustrated by school and wanted to post a video. However, TinyMCE (the visual editor of WordPress) decided to bail on me and stopped loading. I had no choice but to research the problem and found out that mostly it's an issue with the server (boy was I surprised...NOT), and it can be caused by the content provider switching off the _realpath_ function.

The [fix described here](http://wordpress.org/support/topic/123892) didn't work for me though. (It's outdated as well, the file is called _tiny_mce_config.php_ rather _tiny_mce_gzip.ph_ p and it looks completely rewritten. I'm not even sure the realpath function would be an issue anymore.) Apparently it was not StartLogic's fault.

Then I remembered that [Viper's Video Quicktags](http://www.viper007bond.com/wordpress-plugins/vipers-video-quicktags) plugin - which is awesome and lets you post videos with [valid code](http://validator.w3.org/docs/why.html) \- didn't update too well due to [the previously mentioned (QQd) server problems](http://sesam.hu/2008/09/30/miscellaneous-info). I manually updated the plugin and - surprise - everything loaded fine. So... it was the host's fault after all. If the servers hadn't got the speed of a rheumatic snail on sedatives and the stability of a domino tower built onboard a ship in a thunderstorm I'd never have got this error.

Anyway, after a hour or so of googling and fixing (sounds shorter and easier when just blogged about) I'm even more frustrated. And however lame it is to post videos instead of actual posts...

[youtube]http://de.youtube.com/watch?v=DMvl2cWMIOI[/youtube]
