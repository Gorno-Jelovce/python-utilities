# Renames filenames with American MM-DD-YYYY date format
# to European DD-MM-YYYY.

import shutil, os, re

# Create a regex that matches files with american date format
datePattern = re.compile(
    r'''
    ^(.*?)          # all text before the date
    ((0|1)?\d)-     # one or digits for the month
    ((0|1|2|3)?\d)- # one or two digits for the day
    ((19|20)\d\d)   # four digits for the year
    (.*?)$          # all text after the date
''', re.VERBOSE)

# Loop over all files in the current working directory
for amerFilename in os.listdir('.'):
    
    mo = datePattern.search(amerFilename)

    # Skip files without a date
    if mo == None:
        continue

    # Get the different parts of the filename
    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)

    # Form the european style name
    euroFileame = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart

    # Get the full absolute file path
    absWorkingDir = os.path.abspath('.')
    amerFilename = os.path.join(absWorkingDir,amerFilename)
    euroFileame = os.path.join(absWorkingDir,euroFileame)

    # Rename the files
    print(f'Renaming "{amerFilename}" to "{euroFileame}"...')
    #shutil.move(amerFilename,euroFilename)