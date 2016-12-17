import ConfigParser
con = ConfigParser.RawConfigParser()

gmuser = raw_input('What address will this Pi use to send? Format: user@gmail.com > ')
gmpasswd = raw_input('What is the app password for this Gmail account? > ')

con.add_section('gmail')
con.set('gmail', 'user', gmuser)
con.set('gmail', 'password', gmpasswd)
con.set('gmail', 'server', 'smtp.gmail.com:587')

# just fyi, you can path the file relatively. open('../file.cfg' works
with open('gmail.cfg', 'wb') as cfgfile:
    con.write(cfgfile)
