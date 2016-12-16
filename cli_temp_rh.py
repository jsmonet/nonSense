from sense_hat import SenseHat
sense = SenseHat()
import sys
# Start every SenseHat file with this because SenseHat.

def tofahr(celsius):
    return( (celsius/5*9)+32 )

longtemp = tofahr(sense.get_temperature())
longrh = sense.get_humidity()
# And then trim the output to 2 sig figs.
temp = "{0:.1f}".format(longtemp) # I like the shorter format
rh = "{0:.1f}".format(longrh)

# using this with slacktee to CHATOPSZOMG. actually, I want it to 
# notify @channel when the value exceeds a certain value. 

if longtemp > 80:
    print "@channel The temp is " + temp + " and the humidity is " + rh
else:
    print "The temp is " + temp + " and the humidity is " + rh 

# COMMENTS!
