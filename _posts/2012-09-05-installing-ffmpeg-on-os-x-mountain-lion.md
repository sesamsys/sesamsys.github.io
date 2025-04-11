---
layout: post
title: Installing FFmpeg on OS X Mountain Lion
author:
  display_name: sesam
  login: sesam
  email: petersz@me.com
  url: http://sesam.hu
date: '2012-09-05 11:13:55 +0200'
date_gmt: '2012-09-05 09:13:55 +0200'
tags:
- howto
- OS X
- Mountain Lion
- FFmpeg
- Xcode
- Tech &amp; Gizmos
comments:
- id: 10082
  author: 'Underwater Video Tips: Working with AVCHD 2.0 and 1080p60 or 1080p50 files
    in iMovie &laquo; Interceptor121 Underwater Video'
  date: '2013-02-02 22:37:33 +0100'
  date_gmt: '2013-02-02 21:37:33 +0100'
  content: "[...] http://sesam.hu/2012/09/05/installing-ffmpeg-on-os-x-mountain-lion/
    [...]"
---

From time to time I need to do simple jobs with videos, such as a container change. I used to use mencoder for that back on linux and I still think that the versatility of a command line tool is unparalleled by any GUI solution. So I set out to get FFmpeg on my Mac.

There is [a static build available](http://www.evermeet.cx/ffmpeg) from the FFmpeg website, but I decided to take a somewhat more complicated approach and compile it from source myself.

To do so, one first needs **Xcode** , available from the Mac App Store. The current versions, however, do not contain the command line tools needed. A separate package called **Command Line Tools** needs to be installed from either navigating to the Downloads for Apple Developers site from Xcode by _Xcode_ > _Open Developer Tool_ > _More Developer Tools..._ or using the built-in package manager at _Xcode_ > _Preferences..._ on the _Downloads_ tab.

Two packages need to be installed separately first: [LAME](http://sourceforge.net/projects/lame/files) for mp3 encoding (compulsory) and [FAAC](http://www.audiocoding.com/downloads.html) for AAC (optional). The tar.gz files can be unpacked by, for example:
    
    
    tar -xzvf faac-1.28.tar

Then enter their respective directories and issue:
    
    
    ./configure
    make
    sudo make install

Finally, check out the latest source code of FFmpeg:
    
    
    git clone git://source.ffmpeg.org/ffmpeg.git ffmpeg

Compile it with LAME and FAAC enabled (the latter only if it's installed). The `--enable-nonfree` switch is required by FAAC and I got an error unless I disabled Yasm.
    
    
    ./configure --enable-libmp3lame --enable-shared --enable-libfaac --enable-nonfree --disable-yasm
    make
    sudo make install

That's all, FFmpeg is ready to use:
    
    
    Daenerys:Downloads sesam$ ffmpeg
    ffmpeg version N-44141-g9de7622 Copyright (c) 2000-2012 the FFmpeg developers
      built on Sep  4 2012 16:10:11 with llvm-gcc 4.2.1 (LLVM build 2336.11.00)
      configuration: --enable-libmp3lame --enable-shared --enable-libfaac --enable-nonfree --disable-yasm
      libavutil      51. 70.100 / 51. 70.100
      libavcodec     54. 55.100 / 54. 55.100
      libavformat    54. 25.104 / 54. 25.104
      libavdevice    54.  2.100 / 54.  2.100
      libavfilter     3. 15.103 /  3. 15.103
      libswscale      2.  1.101 /  2.  1.101
      libswresample   0. 15.100 /  0. 15.100
    Hyper fast Audio and Video encoder
    usage: ffmpeg [options] [[infile options] -i infile]... {[outfile options] outfile}...
    
    Use -h to get full help or, even better, run 'man ffmpeg'
