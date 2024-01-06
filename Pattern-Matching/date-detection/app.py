import re, pyperclip

# date regex
dateRegex = re.compile(r'''
(0[1-9]|[1-2]\d|3[0-1])  # DD
(/|-|\s)   # /
(0[1-9]|1[1-2])      # MM
(/|-|\s)   # /
(1\d{3}|2\d{3})      # YYYY
''', re.VERBOSE)

# copy clipboard text
text = pyperclip.paste()

matches = []

for groups in dateRegex.findall(text):
    matches.append('/'.join([groups[0], groups[2], groups[4]]))

# paste to clipboard
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print("Matches found: ")
    print('\n'.join(matches))
else:
    print("No matches found")