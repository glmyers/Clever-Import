#!/usr/bin/env python3
'''Python script to rename and move Veracross CSV download files from the user's
Downloads folder to a downloads folder located in the same locations as the
script itself. The script will make the destination folder if it does not
already exist.

The CSV export files are expected to be downloaded immeadiately before the
script is run from Veracross into the user's Downloads folder.

Downloads from other dates will not be moved scince the script only looks for
files ending in 'YYYY-MM-DD.csv' which is the standard Veracross ending.
'''

# import modules used
from os import listdir
from os import path
from os import makedirs
from datetime import date
from shutil import move
from getpass import getuser

# Function to rename and move multiple CSV files exported from Veracross
def vcFiles():
    print()
    if not path.exists('downloads'):
        makedirs('downloads')
    cUser = getuser()
    sourceFolder = f'/Users/{cUser}/Downloads'
    destinationFolder = 'downloads'
    for filename in listdir(sourceFolder):
        if filename[-14:] != f'{date.today()}.csv': continue
        newName = filename[:filename.find(' (')] + '.csv' # assign the new name
        source = f'{sourceFolder}/{filename}'  # original location and name
        destination = f'{destinationFolder}/{newName}' # new location and name
        # rename and move files
        move(source, destination)
        print(f'{newName} moved to downloads')


def main():
    vcFiles()
    return


if __name__ == '__main__':
    main()
