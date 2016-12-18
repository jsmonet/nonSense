import os
import sys
import smtplib
import ConfigParser
from email.mime.text import MIMEText

con = ConfigParser.RawConfigParser()
con.read('gmail.cfg')

fromaddr = con.get('gmail', 'user') 
tostr = con.get('gmail', 'toaddresses')
toaddr = tostr.split()
subject = 'a python test mail'
username = fromaddr
passwd = con.get('gmail', 'password')
server = con.get('gmail', 'server')

msg = MIMEText("""This is just a tribute\nNot the actual song\n\n""")
#msg = """From: %s\nTo: %s\nSubject: %s\n\n%s""" % (fromaddr, toaddr, subject, text)
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
    print 'successfully sent'
except:
    print 'failed miserably'
