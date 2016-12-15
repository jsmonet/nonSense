from astroact import astroact
import sys
from sense_hat import SenseHat
sense = SenseHat()
astroact = astroact()

print "Please select an action from the list:" \
    "1: Temp" \
    "2: rH" \
    "3: Temp & rH"
choice = raw_input("Please enter 1, 2, or 3: ")

if int(choice) == 1:
    astroact.showtemp()
elif int(choice) == 2:
    astroact.showrh()
elif int(choice) == 3:
    astroact.showboth()
else:
    print "you entered an invalid number"
    sys.exit(0)
