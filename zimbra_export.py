#!/usr/bin/python
import pycurl
import sys
import argparse

parser = argparse.ArgumentParser(description="Export a user's mailbox (mail, contacts, calendars) from Zimbra.")
parser.add_argument('-u', '--user', required=True,help="The user's email address/account name.")
parser.add_argument('-p', '--password', help="The user's password.")
args = parser.parse_args()

user = args.user
if args.password:
  passw = args.password
else:
  import getpass
  passw = getpass.getpass()

c = pycurl.Curl();

# Get the mailbox.
f = open(user + '-mailbox.tgz', 'wb')
c.setopt(c.URL, "http://mail.01.com/home/" + user + "?fmt=tgz")
c.setopt(c.USERPWD, user + ":" + passw)
c.setopt(c.WRITEDATA, f)
try:
  c.perform()
except:
  import traceback
  traceback.print_exc(file=sys.stderr)
  sys.stderr.flush()
f.close()

# Close cURL.
c.close()

