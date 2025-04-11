---
layout: post
title: How to make a linux server appear in Finder
author:
  display_name: sesam
  login: sesam
  email: petersz@me.com
  url: http://sesam.hu
date: '2009-04-10 20:41:02 +0200'
date_gmt: '2009-04-10 11:41:02 +0200'
tags:
- AFP
- Avahi
- filesharing
- Gentoo
- linux
- Mac
- netatalk
- osx
comments: []
---

**Update 1:** Added `nss-mdns` service and runlevel defaults.

For a while now I've been battling with the router my ISP gave me. In the name of user-friendliness it has a Japanese administration interface with a lot of katakana for the IT terms. More importantly it simply doesn't offer IP issuance over DHCP based on MAC addresses. Which means with the linux box and the MacBook switched on and off randomly they'd get completely different IP addresses and I have nothing to prevent that.

![router](http://img.skitch.com/20090410-ju8j24exceer5c6ma3y397f5tt.png)

(The MAC Address Filtering only works if the wireless extension is installed, not with wired LAN.)

Now that started being a major nuisance after I shared everything via NFS. OS X can connect to NFS shares with the Command+K "Connect to Server..." option in Finder but it needs the IP address of the machine. I also set up the NFS server to accept connections only from the IP of the MacBook - I don't like open doors - but then that had to be changed as well every time the bloody machines swapped IPs after a restart.

Not too sophisticated.

It recently occurred to me that there must be some implementation of the [zero configuration networking](http://en.wikipedia.org/wiki/Zeroconf) technology of Apple called Bonjour. The idea behind this is that no matter what their IP is machines broadcast the services they offer and find each other on the network without any user interaction whatsoever.

A prime example is when there are two Macs on a network and you set up file sharing on one of them in matter of seconds it will pop up at the "Shared" section of the other's Finder. With Leopard this feature has been extended so Windows machines are recognised automatically as well. When I visited home upon connecting to the LAN the public shares of all the Windows PCs in our house appeared almost instantly. After supplying the usernames and passwords of the respective computers I could browse the files without configuring anything. (You need to set up Samba - well not as much set up more like tick a checkbox in the System Preferences - if you want Windows computers to see Mac shares over the network.)

I think we can all agree that the zeroconf approach is pretty cool. But what if you have a linux box?

Surprisingly it didn't take long at all to figure out a solution. I wonder why I didn't do it earlier to be honest. Here's how it should go on a Gentoo box:

**Step 1** , Set up **netatalk** , the open source implementation of [AFP](http://en.wikipedia.org/wiki/Apple_Filing_Protocol), Apple's file sharing protocol. After emerging it needs a few tweaks. In `/etc/netatalk/netatalk.conf` some protocols are better switched off.

`ATALKD_RUN=no  
PAPD_RUN=no  
CNID_METAD_RUN=yes  
AFPD_RUN=yes  
TIMELORD_RUN=no  
A2BOOT_RUN=no`

Now add the last line to `/etc/netatalk/afpd.conf` to configure the AFP daemon. (Make sure it is one line with no line break.)

`- -transall -uamlist uams_randnum.so,uams_dhx.so -nosavepassword -advertise_ssh`

Then proceed on configuring the shares. They can be added at `/etc/netatalk/AppleVolumes.default` but I just went with the default sharing of the home folder.

With the following command add the netatalk daemon to the default runlevel (so it autostarts every time with the machine) and start it.

`rc-update add atalk default  
/etc/init.d/atalk start`

**Step 2** , Configure **Avahi** , the open source replacement of Bonjour (zero configuration networking). AFP shares is one thing but if you want them to pop in Finder without any hassle you need Bonjour to advertise their presence on the network. Apple has its own source code available for linux but I found mDNSResponder vastly inferior to Avahi. (i.e. I had no idea how it worked...)

Avahi needs a config file at `/etc/avahi/services/afpd.service` to contain the following:

`<?xml version="1.0" standalone='no'?><!--*-nxml-*-->  
<!DOCTYPE service-group SYSTEM "avahi-service.dtd">  
<service-group>  
<name replace-wildcards="yes">%h</name>  
<service>  
<type>_afpovertcp._tcp</type>  
<port>548</port>  
</service>  
<service>  
<type>_device-info._tcp</type>  
<port>0</port>  
<txt-record>model=Xserve</txt-record>  
</service>  
</service-group>`

The txt-record entry specifies the type of machine OS X will think your share is on. This will result in OS X machines to display your linux box with a nice Xserve icon. Undefined shares get an Apple monitor icon or a Windows CRT with BSOD on it as far as I know.

Update 1: In order to be able to use machine names instead of IP addresses from the linux box you will need to emerge the `nss-mdns` package too. In `/etc/nssswitch.conf` find the line starting with `hosts:` and add `mdns` to the end of the line. Mine looks like this now:

`hosts: files dns mdns`

Finally add to the default runlevel and start Avahi as well.

`rc-update add avahi-daemon default  
/etc/init.d/avahi-daemon start`

**Step 3** , **profit**. That's all to it because after starting Avahi an icon for the linux box will appear in matters of seconds in Finder. Press Shift-Command-K to go directly to the Networks location and wait for your server there. When it pops a double click will result in a can't connect error but _don't panic_. Just use the "Connect As..." button and specify your linux username and password. Congratulations, you can now browse the linux server as if it was any other Mac on the network.

![lillemor in osx](http://img.skitch.com/20090410-bqkpw3c2gqwkmpb5rwhdm7ds63.png)

If you want to use more types of services the [Gentoo Wiki page on Avahi](http://en.gentoo-wiki.com/wiki/Avahi) can help with the configurations. If you'd like to use the linux server as a Time Machine backup location [Matthias Kertschmann's guide](http://www.kremalicious.com/2008/06/ubuntu-as-mac-file-server-and-time-machine-volume) explains that as well. My post is based upon his guide except I changed the file locations to their Gentoo equivalents.

It is important to mention that if you run any firewalls on the machines they need to be disabled or adjusted to work with Bonjour/AFP. This mainly means you have to allow communications over port 548 and 5353.
