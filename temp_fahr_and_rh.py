from sense_hat import SenseHat
sense = SenseHat()
# Start every SenseHat file with this because SenseHat.

sense.set_rotation(180)
# It's up on it's side on my desk, USB/Eth ports pointing left
# this makes the output readable for me. I'm setting it up here
# because this file is tiny and containment isn't a big deal

# colors, or colours
red = (255, 0, 0)
yellow = (255, 255, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
aqua = (0, 255, 255)
white = (255, 255, 255)

# SenseHat returns celsius, the temp scale of oppression.
# Let's convert it to glorious units of confusing freedom

def tofahr(celsius):
    return( (celsius/5*9)+32 )

# Freedom done. Let's load a var with that function
longtemp = tofahr(sense.get_temperature())
longrh = sense.get_humidity()
# And then trim the output to 2 sig figs.
temp = "{0:.1f}".format(longtemp) # I like the shorter format
rh = "{0:.1f}".format(longrh)
# And now we'll write it to the LED panel on the SenseHat
# in green because I like green.
if temp < 65.0:
    tempcolour = blue
elif temp >= 65.0 and temp < 70.0:
    tempcolour = aqua
elif temp >= 70.0 and temp < 76.0:
    tempcolour = green
elif temp >= 76.0 and temp < 80.0:
    tempcolour = yellow
else:
    tempcolour = red

if rh < 15:
    rhcolour = red
elif rh >= 15 and rh < 20:
    rhcolour = yellow
elif rh >= 20 and rh < 30:
    rhcolour = aqua
elif rh >= 30 and rh < 50:
    rhcolour = green
elif rh >= 50 and rh < 70:
    rhcolour = yellow
else:
    rhcolour = red

sense.show_message(temp + "F ", text_colour=tempcolour)
sense.show_message("& ", text_colour=white)
sense.show_message(rh + "%rH", text_colour=rhcolour)

# COMMENTS!
