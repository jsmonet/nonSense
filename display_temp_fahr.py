from sense_hat import SenseHat
sense = SenseHat()
sense.set_rotation(180)
def tofahr(celsius):
    return( (celsius/5*9)+32 )

longtemp = tofahr(sense.get_temperature())
temp = "{0:.2f}".format(longtemp) 
sense.show_message(temp, text_colour=[0, 255, 0])
