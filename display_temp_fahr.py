import sys
from sense_hat import SenseHat
sense = SenseHat()
# Start every SenseHat file with this because SenseHat.
if len(sys.argv) > 1:
    rot = sys.argv[1]
else:
    rot = '180'

if not rot or rot is '180':
    sense.set_rotation(180)
elif rot is "90":
    sense.set_rotation(90)
elif rot is '0':
    sense.set_rotation()
elif rot is "270":
    sense.set_rotation(270)
else: # anything else typed in here at all. 
    sense.set_rotation(0) # because cheating 

# It's up on it's side on my desk, USB/Eth ports pointing left
# this makes the output readable for me. I'm setting it up here
# because this file is tiny and containment isn't a big deal

# SenseHat returns celsius, the temp scale of oppression.
# Let's convert it to glorious units of confusing freedom

def tofahr(celsius):
    return( (celsius/5*9)+32 )

# Freedom done. Let's load a var with that function
longtemp = tofahr(sense.get_temperature())
# And then trim the output to 2 sig figs.
temp = "{0:.2f}".format(longtemp)

# And now we'll write it to the LED panel on the SenseHat
# in green because I like green.
sense.show_message(temp, text_colour=[0, 255, 0])

# COMMENTS!
