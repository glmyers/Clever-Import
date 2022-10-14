# Clever-Import
Python script to automate the creation of upload files for Clever from Veracross exports. Note the Veracross export files should be in CSV format and come from queries utilizing the names below. Note that the students query utilized checks to ensure only students with a school email address are exported. Not all our students have functioning email in our system, but they all have an address assigned. Nonfunctioning addresses are store in the 'Email 2' of their record to avoid bounce list issues. The 'gradesNoEmail' funtion in the 'fieldList.py' file is used in the script to ensure the correct email field from the export is used. This fuction is in this file for ease of editing the grades since it email is activated for some grades during the school year. If your school only uses 'Email 1' you can simply delete all grades leaving an empty list. 
## Veracross export files
The script expects five CSV export files from the Veracross school information system in a folder named "downloads" in the current working directory. The 'renameExports.py' script will move exported CSV files from the user's Downloads into the correct folder in the working directory while also striping off the information appeded to query names when downloading CSV files.  
* adminsC.csv - (*from an export Find Staff/Faculty query using a Profile Code to distinguish addmins 328516*)
* enrollmentsC.csv - (*from an export of a Find Class Enrollment Records query 325696*)
* sectionsC.csv - (*from an export of a Class Permission query 325726*)
* studentsC.csv - (*from an export of a Find Students query 328467 must be edited to use your domain*)
* teachersC.csv - (*from an export Find Staff/Faculty query 328480*)

The results of the script intended to be in a folder named "uploadClever" in the same folder where the script files are located. The names of the Veracross export files and the locations of both input files and output files is set in the "main" function of the script and is easily edited if needed by the individual user.
## Headers of the files for importing
The file fieldsList.py identifies the field names required in the header row of csv import files for Clever. This file is used by the script creating the files for importing and must be in the same directory as uploadClever.py when it is run. Running this file itself merely outputs a listing of all the field names to the terminal window. The output of field names does also identify which ones are required by Clever to have a successful import.

## Schools not included
The schools.csv file needs to exist, but due to its static nature it is manually creaded and placed in the uploadClever file which is the synchronized to the Clever server. I've not updated it in years, but your situation may be different.
