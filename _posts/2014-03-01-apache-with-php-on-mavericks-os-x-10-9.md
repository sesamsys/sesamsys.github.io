---
layout: post
title: Apache with PHP on Mavericks (OS X 10.9)
author:
  display_name: sesam
  login: sesam
  email: petersz@me.com
  url: http://sesam.hu
date: '2014-03-01 20:47:34 +0100'
date_gmt: '2014-03-01 19:47:34 +0100'
tags:
- hack
- OS X
- server
- Apache
- Mavericks
- PHP
- Tech &amp; Gizmos
comments:
- id: 14756
  author: sld
  date: '2014-04-15 19:44:35 +0200'
  date_gmt: '2014-04-15 17:44:35 +0200'
  content: "Ha szeretnél esetleg tovább geek-ülni (és továbblépni a PHP-n), szerintem
    nézz utána a Jekyll-nek: http://jekyllrb.com/\r\n\r\nOldalam is ebben készült.
    Nekem nagyon megfelel hogy statikus, ellenben értelmezhető formában írom. A dinamikus
    dolgokat már úgyis régen megoldotta az analytics, a disqus, mindenféle egyéb on-demand
    szolgáltatás.\r\n\r\nPélda content: https://github.com/sldblog/sldblog.github.io/blob/master/_posts/sldcode/2014-04-01-mktime-off-by-millisecond.md\r\nSzép
    szerkesztő is van azért: https://stackedit.io/"
- id: 14833
  author: SeSam
  date: '2014-04-17 15:08:09 +0200'
  date_gmt: '2014-04-17 13:08:09 +0200'
  content: Mik vannak! :O
---

Ha már annyira kockára sikerült a szombat, hogy lokálban telepítek WordPresst, pár feljegyzés:

Bár az Apple kivette a Preferencesből, az Apache azért harcra készen ott van a rendszerben, csupán a következő paranccsal el kell indítani:
    
    
    sudo apachectl start

Ha pedig PHP-re is szükség van benne, akkor az alábbi fájlban kell kikommentezni a jelzett sort, majd újraindítani a szervert:
    
    
    /etc/apache2/httpd.conf
    
    
    LoadModule php5_module libexec/apache2/libphp5.so

Profit.
