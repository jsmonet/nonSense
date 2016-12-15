This all written for a Sense Hat on an RPi 3.

Check out http://pythonhosted.org/sense-hat/ for info on the Sense Hat api. It's dead simple to use once you have it installed and play around with it a bit.

To set up your Pi3 already running [Raspbian](https://www.raspberrypi.org/downloads/raspbian/ "Raspbian"), run:

~~~~
sudo apt-get update
sudo apt-get install sense-hat
sudo reboot
~~~~

This is taken directly from the link above.

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
