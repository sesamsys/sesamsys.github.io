---
layout: post
title: 'flightradar'
author:
  display_name: sesam
tags:
- flightradar
- flying
- aviation
- bash
- coding
- ChatGPT
---

I opted in to provide data to [flightradar24](https://www.flightradar24.com/) which has several benefits, the best of which is that I get a Business subscription for free. The stuff runs on a software-defined radio receiver connected to a Raspberry Pi.

Unfortunately — unknown to me as to why —  the software can become flaky and disconnect without notifying me. So I made it my mission to have some sort of monitoring.

There’s a command — fr24feed-status — that reports on what’s going on. An example output looks like this:

{% highlight shell %}
{% raw %}
  sesam in 🌐 bringebaer in ~ via 🐍 v3.9.2
  ❯ fr24feed-status
    FR24 Feeder/Decoder Process: running.
    FR24 Stats Timestamp: 2023-01-20 16:30:21.
    FR24 Link: connected [UDP].
    FR24 Radar: T-ESSB413.
    FR24 Tracked AC: 3.
    Receiver: connected (367616 MSGS/0 SYNC).
    FR24 MLAT: ok [UDP].
    FR24 MLAT AC seen: 1.
{% endraw %}
{% endhighlight %}

Whenever any of the responses contains “Failed” something went awry, that’s when I wanted a notification. Problem #1, I don’t speak bash. Enter ChatGPT, and the question: *write a bash script that runs fr24feed-status and if the result contains Failed then email X*.

It’s actually not that hard, could have learned myself…

{% highlight shell %}
{% raw %}
  sesam in 🌐 bringebaer in ~ via 🐍 v3.9.2
  ❯ cat fr24feed-alert.sh
    #!/bin/bash

    # Run fr24feed-status and save the output
    status=$(fr24feed-status)

    # Check if the output contains "Failed"
    if [[ $status == *"Failed"* ]]
    then
    # Send an email to petersz@me.com
    echo "$status" | mailx -s "fr24feed Status Failed" petersz@me.com
    fi
{% endraw %}
{% endhighlight %}

The most complex bit was to make sure that the Raspberry can send actual emails. Mailx is your friend. You need an application password and a configuration file to succeed.

So far it’s been stable so needs testing. 😅