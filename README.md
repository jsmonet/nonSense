This all written for a Sense Hat on an RPi 3.

Check out http://pythonhosted.org/sense-hat/ for info on the Sense Hat api. It's dead simple to use once you have it installed and play around with it a bit.

To set up your Pi3 already running [Raspbian](https://www.raspberrypi.org/downloads/raspbian/ "Raspbian"), run:

~~~~
sudo apt-get update
sudo apt-get install sense-hat
sudo reboot
~~~~

This is taken directly from the link above.

**The "why"**

I'm using this project to run multiple rpi in a datacenter for some out of band monitoring and haaaated needing to set up yet another bunch of snmp traps plus spend a week cabling up all of the LCP in our Rittal IRC system. It's a great system--a bunch of air-water heat exchangers spaced every 2 cabs with full environmental monitoring...running windows CE. Well, yeah, there ya go. Instead of spending the time and money getting all that copper run, I'm dropping a handful of these minions into specific cabs and keeping our internal documentation tight with their locations. Additionally, I've set up key distro via config management and am laying down the various unique files via templates placed by the same config management.

**How to use:**

Not every file in this repo is useful. In fact, most aren't. On top of that you'll likely be missing some files by just cloning. Let's get started.

1. Clone the repo to /opt/nonSense on your Pi. If you have trouble with this step... don't have trouble with this step
* Make sure you have the necessary packages installed. `apt-get install python-pip sense-hat` and restart if necessary
* If you are looking to use email notification and you are not using config management, go into /opt/nonSense and run smtpcfg_builder.py. This will generate /opt/nonSense/gmail.cfg. Obviously I wrote this for use with a 2fa-enabled gmail account using an app password.
* For slack integration, go grab the slacktee repo and put `slacktee.sh` in `/usr/local/bin` as `/usr/local/bin/slacktee` and make sure you edit the default config in that file, or place a `.slacktee` in the home folder of your service account

Most everything is either currently, or will soon reference `astroact.py`. I have to take off right meow, so this will get more attention in a few days. <3

**Resources I'm using**
http://cloford.com/resources/colours/500col.htm

The colours! Using brit spelling because the API also deploys the U of doom. Er... dooum?

I'm only including this link so I don't have to search it in the future.

Something to copypasta into files for simple color declaration:

~~~~
red = (255, 0, 0)
yellow = (255, 255, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
aqua = (0, 255, 255)
white = (255, 255, 255)
~~~~

**Use of the files in this repo:**

Python 2.7.x is my jam. If you use Python3 on **show_text.py** it will throw an error because I didn't write it for 3. SO LAZY I know.

**display_temp_fahr.py** is simply run. I prefer to run it explicitly with `python` like this:

`python display_temp_fahr.py`

As you can glean from the name of the file, this takes the celsius data returned from the SenseHat's temp sensor and converts it to fahrenheit

Digging in, this bit:
```Python
temp = "{0:.2f}".format(longtemp)
```
limits the significant figures to 2.



**show_text.py** takes one or two arguments. Arg1 is a string displayed on the LED panel of the Sense Hat. Arg2 is the rotation. So, lettuce running:

`python show_text.py "quote-wrapped text" 270`

This will display quote-wrapped text, rotated 270 degrees.

Alright, I've commented the files out in my typical moderately helpful, yet supremely crass manner.

**testactions.py** prompts cli for what you want to do. I plan to use this as a basis for joystick-driven reactions. The scheme is down and repeatable now. Calls astroact.py in the same dir

**astroact.py** called by testactions.py. It has a lot of globals, and I'm not hugely jazzed about that, but they are limited to the file so it's not SUCH a huge deal at this moment, running on a pi, where it will always live.

I'll write a joystick.py soon to trigger these events. I want to make it a systemd unit and have it idle.

Just tucking this right here for the email config builder to work.

sudo pip install validate_email

sudo pip install pyDNS

You need to pip install as root the above packages in order for validate_email to work AND validate the legitimacy of the addresses

**But wait, there are holes**

Yeah, I wanted to python up the entire load-in, but we use [Puppet](http://www.puppet.com) for config management and rockin an ERB for these little holes is just WAY easier.

To give you an idea of how these are set up, scope my puppet:

~~~~
# packages first
package { 'git':
  ensure => installed,
}
package { 'python-pip':
  ensure => installed,
}
package { 'pyDNS':
  ensure   => installed,
  provider => 'pip',
  require => Package['python-pip'],
}
package { 'validate_email':
  ensure   => installed,
  provider => 'pip',
  require => Package['python-pip'],
}
package { 'sense-hat':
  ensure   => installed,
}
vcsrepo { '/opt/nonSense':
  ensure   => latest,
  provider => git,
  excludes => ['.git', '.gitignore'],
  source   => 'https://github.com/jsmonet/nonSense.git',
  require  => Package['git'],
}
# set slacktee vars for erb
# this works just fine. Only reason to pull from the repo again would
# be to fix security issues with slacktee.
$slackchan = 'viruses'
$slackname = "Pi in $hostname"
file { '/usr/local/bin/slacktee':
  ensure   => file,
  content  => template('fury/slacktee_dot_sh.erb'),
  mode     => '0755',
}
cron { 'monitoring':
  command => "/usr/bin/python /opt/nonSense/tf_dis_slack.py 180",
  user => 'root',
  minute => '*/1',
}
~~~~

You'll notice, if you're digging around
