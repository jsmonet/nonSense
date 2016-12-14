import astroact
import sys

print "Please select an action from the list:" \
    "1: Temp" \
    "2: rH" \
    "3: Temp & rH"
choice = raw_input("Please enter 1, 2, or 3: ")

if choice == 1:
    astroact.showtemp()
elif choice == 2:
    astroact.showrh()
elif choice == 3:
    a = astroact.showtemp()
    b = astroact.showrh()
    print a + " & " + b
else:
    print "you entered an invalid number"
    sys.exit(0)
