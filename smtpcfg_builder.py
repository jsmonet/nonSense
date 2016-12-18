import os.path # to test file existence 
import sys
from validate_email import validate_email # because we want to be sure
import ConfigParser
con = ConfigParser.RawConfigParser()

def get_gm_user():
    global gmuser
    gmuser = raw_input('What address will this Pi use to send? Format: user@gmail.com > ')
    while not gmuser:
        gmuser = raw_input('You entered nothing. What address will this Pi use to send? Format: user@gmail.com > ')
    gvalid = validate_email(gmuser,verify=True)
    while not gvalid:
        gmuser = raw_input('Email address verification failed. Please enter a valide email address > ')
        gvalid = validate_email(gmuser,verify=True)
    return gmuser

def get_gm_passwd():
    global gmpasswd
    gmpasswd = raw_input('What is the app password for this Gmail account? > ')
    while not gmpasswd:
        gmpasswd = raw_input('You entered nothing. What is the app password for this Gmail account? > ')
    return gmpasswd

def make_cfg_file():
    try:
        get_gm_user()
        get_gm_passwd()
        con.add_section('gmail')
        con.set('gmail', 'user', gmuser)
        con.set('gmail', 'password', gmpasswd)
        con.set('gmail', 'server', 'smtp.gmail.com:587')
        # just fyi, you can path the file relatively. open('../file.cfg' works
        with open('gmail.cfg', 'wb') as cfgfile:
            con.write(cfgfile)
    except KeyboardInterrupt:
        print "You hit ctrl-c. Exiting"
        sys.exit(0)

try:
    if os.path.isfile('gmail.cfg'):
        print "File 'gmail.cfg' already exists"
        shouldstilldo = raw_input('Would you like to proceed and overwrite the file? [y]es or [n]o. default: [y]') or "y"
        while not shouldstilldo in ['y', 'Y', 'n', 'N']:
            shouldstilldo = raw_input('Would you like to proceed and overwrite the file? [y]es or [n]o. default: [y]') or "y"
        if shouldstilldo in ['y', 'Y']:
            make_cfg_file()
        elif shouldstilldo in ['n', 'N']:
            print "Ok, exiting"
            sys.exit(0)
        else:
            print "You broke the matrix. Impressive. Go away now"
            sys.exit(0)
    else:
        make_cfg_file()
except KeyboardInterrupt:
   sys.exit(0)
