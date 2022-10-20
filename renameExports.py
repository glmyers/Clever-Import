#!/usr/bin/env python3
'''Python script to rename and move Veracross CSV download files from the
Downloads folder in the user's home directory to a downloads folder located in
the same locations as the script itself. The script will make the destination
folder if it does not already exist.

The CSV export files are expected to be downloaded immeadiately before the
script is run from Veracross into the user's Downloads folder.

Downloads from other dates will not be moved scince the script only looks for
files ending in 'YYYY-MM-DD.csv' which is the standard Veracross ending where
the date is the date of the export.
'''

# import modules used
from os import listdir
from os import makedirs
from datetime import date
from shutil import move
from pathlib import Path

# Function to rename and move multiple CSV files exported from Veracross
def vcxFiles():
    print()
    if not Path('downloads').is_dir():
        makedirs('downloads')
    sourceFolder = f'{Path.home()}/Downloads'
    destinationFolder = 'downloads'
    for filename in listdir(sourceFolder):
        if filename[-14:] != f'{date.today()}.csv': continue
        newName = filename[:filename.find(' (')] + '.csv' # assign the new name
        source = f'{sourceFolder}/{filename}'  # original location and name
        destination = f'{destinationFolder}/{newName}' # new location and name
        # rename and move files
        move(source, destination)
        print(f'{newName} moved to downloads')
        print()

def main():
    vcxFiles()
    return


if __name__ == '__main__':
    main()
