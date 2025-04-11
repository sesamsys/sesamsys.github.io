---
layout: post
title: iStat Pro fix
author:
  display_name: sesam
  login: sesam
  email: petersz@me.com
  url: http://sesam.hu
date: '2013-01-02 16:27:17 +0100'
date_gmt: '2013-01-02 15:27:17 +0100'
tags:
- Bjango
- fix
- OS X
- widget
- iStat
- Tech &amp; Gizmos
comments: []
---

Régóta használom az [iStat Pro](https://www.apple.com/downloads/dashboard/status/istatpro.html) widgetet OS X-en. Kiváló arra, hogy egy gyors mozdulattal rá lehessen tekinteni a szabad tárhelyre, a memória állapotára, vagy hogy melyik processz zabálja épp a CPU-t. Mivel a Dashboardon ül, máskor nem zavar fölöslegesen ezekkel.

Sajnos a Bjango már nem fejleszti a terméket, a kiváltására ajánlott [iStat Menus](http://bjango.com/mac/istatmenus) pedig nekem nem tetszik, és drága is. Viszont Mountain Lion alatt eltört a widget folyamatokat listázó része...

Szerencsére [találtam egyszerű javítást hozzá](http://forums.macrumors.com/showpost.php?p=15332289&postcount=20):

  1. Keresd meg a widgetet a **~/Library/Widgets** (esetleg a **/Library/Widgets** ) könyvtárban.  
Ha nem megy, Finderben a Shift + Command + G nyitja meg ezeket.
  2. Jobb kattintás után válaszd a **Show Package Contents** opciót.
  3. Nyisd meg a **Wide.js** (horizontális nézet) vagy a **Tall.js** (vertikális nézet) filet.
  4. Az alábbi sorokban a " **PID|$1** " részeknél a pipe | után kell írni egy spacet: " **PID| $1** " 
    
        if(p.v("processes_sort_mode") == 'cpu')
    		widget.system('ps -arcwwwxo "pid %cpu command" | egrep " **PID| $1** " | grep -v grep | ' + exclude + ' head -7 | tail -6 | awk \'{print ""$1""$2""$3,$4,$5""}\'', function(data){ _self.updateProcessesOut(data);});
    	else
    		widget.system('ps -amcwwwxo "pid rss command"  | egrep " **PID| $1** " | grep -v grep | ' + exclude + ' head -7 | tail -6 | awk \'{print ""$1""$2""$3,$4,$5""}\'', function(data){ _self.updateProcessesOut(data);});
    }

  5. Mentés után a widget eltávolításával, majd újra Dashboardhoz adásával már helyesen listázódnak a processzek.
