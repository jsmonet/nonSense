from astroact import astroact
import sys
from sense_hat import SenseHat
sense = SenseHat()
astroact = astroact()

print "Please select an action from the list:\n" \
    "1: Temp\n" \
    "2: rH\n" \
    "3: Temp & rH\n" \
    "4: Slack the value\n"

choice = input("Please enter 1, 2, 3: or 4: ")

if choice == 1:
    astroact.showtemp()
elif choice == 2:
    astroact.showrh()
elif choice == 3:
    astroact.showboth()
elif choice == 4:
    astroact.slacktemp()
else:
    print "you entered an invalid number"
    sys.exit(0)
