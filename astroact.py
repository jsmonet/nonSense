import sys
import subprocess
import platform
from sense_hat import SenseHat
import smtplib
import configparser
from email.mime.text import MIMEText
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
   
    def tofahr(self):
        tempc = sense.get_temperature()
        return ( (tempc/5*9)+32)
    
    def showtemp(self):
        longtemp = astroact.tofahr(self)
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
            print ("Killed")
            sense.clear() # clear the LED
            sys.exit(0) # no need for a non-clean exit code
    
    def getvals(self):
        longtemp = astroact.tofahr(self)
        temp = "{0:.1f}".format(longtemp) # I like the shorter format
        longrh = sense.get_humidity()
        rh = "{0:.1f}".format(longrh)
        values = "Temp is {0}F and rH is {1}%".format(temp, rh)
        return values

    def slackit(self, message):
        cmd ="echo " + str(message) + " | /usr/local/bin/slacktee"
        aps = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        aps = aps.communicate()[0]
        print (aps)
  
    def slacktemp(self):
        cmd ="/usr/bin/python /opt/nonSense/cli_temp_rh.py | /usr/local/bin/slacktee"
        ps = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        ps = ps.communicate()[0]
        print (ps)

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
            print ("Killed")
            sense.clear()
            sys.exit(0)

    def showboth(self):
        try:
            astroact.showtemp(self)
            sense.show_message("&", text_colour=white)
            astroact.showrh(self)
        except KeyboardInterrupt:
            print ("Killed")
            sense.clear()
            sys.exit(0)

    def temprhslack(self):
        ctemp = sense.get_temperature()
        crh = sense.get_humidity()
        try:
            if ctemp > 26.667 or crh > 55: 
                astroact.slacktemp(self)
            elif ctemp > 29.44 or crh > 65:
                astroact.slacktemp(self)
                alertmsg = str(astroact.getvals(self))
                astroact.mailer(self, alertmsg)
            astroact.showtemp(self)
            sense.show_message("&", text_colour=white)
            astroact.showrh(self)
        except KeyboardInterrupt:
            print ("Killed")
            sense.clear()
            sys.exit(0)

    def mailer(self, message):
        con = ConfigParser.RawConfigParser()
        con.read('gmail.cfg')
        piname = platform.node()
        fromaddr = con.get('gmail', 'user')
        tostr = con.get('gmail', 'toaddresses')
        toaddr = tostr.split(',')
        subject = "Cab %s value out of range" % piname 
        username = fromaddr
        passwd = con.get('gmail', 'password')
        server = con.get('gmail', 'server')
        msg = MIMEText(message) 
        msg['Subject'] = subject
        msg['From'] = fromaddr
        msg['To'] = tostr

        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.ehlo()
            server.starttls()
            server.login(username, passwd)
            server.sendmail(fromaddr, toaddr, msg.as_string())
            server.close()
            print ('successfully sent')
        except:
            print ('failed miserably')


    def sensewithalerts(self):
        ctemp = sense.get_temperature()
