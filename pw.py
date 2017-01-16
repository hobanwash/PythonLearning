#! python3
# pw.py - An insure password locker

PASSWORDS = {'email': '1234',
             'facebook': '12345',
             'twitter': '12345'}

import sys, pyperclip
if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]   # first command line arg is the account name

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' has been copied to the clipboard')
else:
    print('There is no record for ' + account)

