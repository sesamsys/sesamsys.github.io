---
layout: post
title: Parancssoros AirPort
author:
  display_name: sesam
  login: sesam
  email: petersz@me.com
  url: http://sesam.hu
date: '2011-11-10 21:30:28 +0100'
date_gmt: '2011-11-10 20:30:28 +0100'
tags:
- airport
- apple
- Mac
- osx
- WiFi
- channel
- Tech &amp; Gizmos
comments:
- id: 5408
  author: sld
  date: '2011-11-10 23:06:10 +0100'
  date_gmt: '2011-11-10 22:06:10 +0100'
  content: mitleselribanc SSID :)
- id: 5419
  author: Youkai
  date: '2011-11-11 10:02:07 +0100'
  date_gmt: '2011-11-11 09:02:07 +0100'
  content: "Vegyél Linksys vagy TP-Link N-es wifi routert az én tp linkem a földszinten
    fogható a betonon keresztül jah a 4. emeleten lakom... a többi lakos meg megoldja
    a wifi-t :). \r\nMondjuk felénk sok a nyugdíjas, szóval nincs zavaró adóállomás,
    max a távfűtóművek wifi-s kis-központ ellenőrző rendszere van :)"
- id: 5420
  author: Youkai
  date: '2011-11-11 10:04:45 +0100'
  date_gmt: '2011-11-11 09:04:45 +0100'
  content: "Jah, nem is tudtam, hogy ilyen jó kis céged van :P\r\nhttp://www.sesamnet.ch/"
---

Nem tudom, megírta-e már valaki magyarul, mindenesetre ezt most elteszem ide, később biztos hasznos lesz.

Nem egy közismert dolog, hogy OS X alatt a vezetéknélküli kapcsolatokkal parancssorból is lehet dolgozni. Az `airport` parancs az alábbi könyvtárba van eldugva:
    
    
    /System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/

A `-I` kapcsolóval a jelenlegi kapcsolatról szolgáltat információt:
    
    
    $ ./airport -I
         agrCtlRSSI: -66
         agrExtRSSI: 0
        agrCtlNoise: -92
        agrExtNoise: 0
              state: running
            op mode: station 
         lastTxRate: 65
            maxRate: 130
    lastAssocStatus: 0
        802.11 auth: open
          link auth: wpa2-psk
              BSSID: 0:1f:f3:6:34:1
               SSID: SeSamNet
                MCS: 7
            channel: 11

A `-s` pedig kilistázza a csatlakozható hálózatokat:
    
    
    $ ./airport -s
                                SSID BSSID             RSSI CHANNEL HT CC SECURITY (auth/unicast/group)
                         T-home anna 00:1c:a2:df:70:1f -89  6       N  -- WPA(PSK/TKIP,AES/TKIP) WPA2(PSK/TKIP,AES/TKIP) 
                             Pirelli 00:1c:a2:fe:61:80 -81  6       N  -- WPA(PSK/TKIP,AES/TKIP) WPA2(PSK/TKIP,AES/TKIP) 
                       lengyeldallos 70:71:bc:e9:e8:2e -92  6       Y  -- WPA(PSK/AES,TKIP/TKIP) WPA2(PSK/AES,TKIP/TKIP) 
                      Discus--16C7C5 38:22:9d:16:c7:c5 -81  6       N  -- WPA(PSK/TKIP,AES/TKIP) WPA2(PSK/TKIP,AES/TKIP) 
                      mitleselribanc 00:25:86:e2:8c:1a -82  6       N  -- WPA2(PSK/TKIP,AES/TKIP) 
                              apollo 00:15:e9:de:eb:55 -91  6       N  -- WPA(PSK/TKIP/TKIP) 
                          Poret Home 00:1f:9f:cc:e1:ed -91  1       N  -- WPA(PSK/AES,TKIP/TKIP) WPA2(PSK/AES,TKIP/TKIP) 
                              Takumi 00:23:cd:13:d5:a0 -81  1       N  -- WPA2(PSK/TKIP,AES/TKIP) 
                              87c9ca e0:69:95:1c:e8:b5 -86  1       Y  -- WPA(PSK/AES,TKIP/TKIP) WPA2(PSK/AES,TKIP/TKIP) 
              OPUTAGODWIN-PC_NETWORK 74:ea:3a:a2:a7:78 -87  11,-1   Y  -- WPA(PSK/AES/AES) WPA2(PSK/AES/AES) 
                        T-HomeGyorgy 00:1c:a2:df:f4:ff -85  12      N  -- WEP
                            SeSamNet 00:1f:f3:06:34:01 -54  11      Y  JP WPA2(PSK/AES/AES) 
                     RÉKA-PC_Network 00:27:19:e9:08:8e -89  11,-1   Y  -- WPA2(PSK/AES/AES) 
              Gábor Pluhárs Netzwerk d8:30:62:36:cb:d3 -78  11      Y  HU WPA2(PSK/AES/AES)

A fentiekből látható, hogy sajnos nincs olyan [csatorna](http://en.wikipedia.org/wiki/List_of_WLAN_channels), ahol zavarás nélkül lehetne wifizni, túl sokan vagyunk hozzá:

[![Non-overlapping WLAN channels](http://upload.wikimedia.org/wikipedia/commons/thumb/8/84/NonOverlappingChannels2.4GHzWLAN-en.svg/600px-NonOverlappingChannels2.4GHzWLAN-en.svg.png)](http://en.wikipedia.org/wiki/List_of_WLAN_channels)
