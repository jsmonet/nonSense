import sys
from astroact import astroact
from sense_hat import SenseHat
sense = SenseHat()
astro = astroact()
# Start every SenseHat file with this because SenseHat.

if len(sys.argv) > 1:
    rot = sys.argv[1]
else:
    rot = "0"

if rot in ['0', '90', '180', '270']:
    sense.set_rotation(int(rot))
else:
    sense.set_rotation()

try:
    astro.temprhslack()
except KeyboardInterrupt:
    print ("Killed")
    sense.clear() # clear the LED
    sys.exit(0) # no need for a non-clean exit code

# COMMENTS!
