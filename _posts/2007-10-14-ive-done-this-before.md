---
layout: post
title: I&#039;ve done this before...
author:
  display_name: sesam
  login: sesam
  email: petersz@me.com
  url: http://sesam.hu
date: '2007-10-14 10:54:26 +0200'
date_gmt: '2007-10-14 01:54:26 +0200'
tags:
- backup
- dotmac
- idisk
- itunes
- Mac
- nfs
- Tech &amp; Gizmos
comments: []
---

I managed to import the songs properly to iTunes finally.

(For non-Hungarian speakers, the last post was about me being unable to change the ID3 info of a couple of songs in iTunes. I could rewrite the tags all right, it just got changed back whenever I restarted iTunes.)

Googling the problem revealed that apparently other people have encountered the same bug, but I couldn't find any decent solution. So I just copied the songs to Linux, rewrote the ID3s in Audacious and imported them back. It worked.

But in order to do that I had to set up the NFS. And NFS requires that the uids of the users are the same on both machines so I had to change my uid on the MacBook. (Following [this guide](http://lissot.net/netinfo/change_user.html).)

(I could have sworn I wrote a blog post about this when I first did it. Couldn't seem to find the post though.)

See how every problem generates a new one?

Anyway, I also managed to get my backup of the Documents folder restored from iDisk. (It's basically some storage space on Apple's servers that comes with the .Mac subscription.) I really don't know what divine enlightenment possessed me at that moment, but I set up a daily backup for the documents on the Mac using the .Mac Backup 3 tool a while ago. Probably I just wanted to try the backup software...

The technology is the following: at the start it creates an archive then whenever a file is changed it creates a so-called increment file. This way only the changes are saved greatly reducing the disk space needed.

However possibly because of .Mac being unbearably slow the process of restoring from a backup takes ages. And Backup 3 isn't really offering much feedback either, other than the rainbow cursor of death. I guess it has to check through every single increment file and reading those takes time. They could have put a progress bar there or something though, because it really looks like it just hung. For several minutes. And I mean several.

Then when it finally starts copying the files back the progress bar has the nasty habit of disappearing for - once again - extended periods of time.

I can't complain though because it really did copy everything back.

However, the best part was when I removed the old backups from iDisk. Again, it worked without a glitch - took bloody ages of course - but it displayed something like this:

<figure>
  <img src="http://www.sesam.hu.php5-19.dfw1-2.websitetestlink.com/wp-content/uploads/2007/10/dotmac_weirdness.png" alt=".Mac acting up">
  <figcaption>.Mac acting up</figcaption>
</figure>
