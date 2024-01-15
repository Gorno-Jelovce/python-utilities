#! python3
# mapIt.py - Launches a map in the browser using an address from
# command line or clipboard.

import webbrowser, sys, pyperclip

if len(sys.argv) > 1:
    # Get address form command line.
    address = ' '.join(sys.argv[1:])
else:
    # Get address form clipboard
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)