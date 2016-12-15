import sys
from sense_hat import SenseHat
sense = SenseHat() # Start every SenseHat file with this because SenseHat.


class astroact:
    # colors, or colours
    global red
    red = (255, 0, 0)
    global yellow
    yellow = (255, 255, 0)
    global green
    green = (0, 255, 0)
    global blue
    blue = (0, 0, 255)
    global aqua
    aqua = (0, 255, 255)
    global white
    white = (255, 255, 255)
    
    sense.set_rotation(180) # set rotation here because these functions' outputs do not inherit rotation spec from other files importing this one
    
    def showtemp(self):
        def tofahr(celsius):
            return ( (celsius/5*9)+32)
        longtemp = tofahr(sense.get_temperature())
        temp = "{0:.1f}".format(longtemp) # I like the shorter format
        if longtemp < 65.0:
            tempcolour = blue
        elif longtemp >= 65.0 and longtemp < 70.0:
            tempcolour = aqua
        elif longtemp >= 70.0 and longtemp < 76.0:
            tempcolour = green
        elif longtemp >= 76.0 and longtemp < 80.0:
            tempcolour = yellow
        else:
            tempcolour = red
        try:
            sense.show_message(temp + "F ", text_colour=tempcolour)
        except KeyboardInterrupt:
            print "Killed"
            sense.clear() # clear the LED
            sys.exit(0) # no need for a non-clean exit code 

    def showrh(self):
        longrh = sense.get_humidity()
        # And then trim the output to 2 sig figs.
        rh = "{0:.1f}".format(longrh)
        # And now we'll write it to the LED panel on the SenseHat
        # in green because I like green.

        if longrh < 15:
            rhcolour = red
        elif longrh >= 15 and longrh < 20:
            rhcolour = yellow
        elif longrh >= 20 and longrh < 30:
            rhcolour = aqua
        elif longrh >= 30 and longrh < 50:
            rhcolour = green
        elif longrh >= 50 and longrh < 70:
            rhcolour = yellow
        else:
            rhcolour = red
        try:
            sense.show_message(rh + "%rH", text_colour=rhcolour)
        except KeyboardInterrupt:
            print "Killed"
            sense.clear()
            sys.exit(0)

    def showboth(self):
        try:
            astroact.showtemp(self)
            sense.show_message("&", text_colour=white)
            astroact.showrh(self)
        except KeyboardInterrupt:
            print "Killed"
            sense.clear()
            sys.exit(0)
