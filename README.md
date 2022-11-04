# Clever-Import
Python script to automate the creation of upload files for Clever from Veracross exports. Note the Veracross export files should be in CSV format and come from queries utilizing the names below. The working directory should be the one containing this script.
## Domain and Email
Export files from Veracross need to contain both __Email 1__ and __Email 2__. Not all our students have functioning email in our system, but they all have an address assigned. Nonfunctioning addresses are stored in the __Email 2__ of their record to avoid bounce list issues.
The 'domain' global variable located under the import statements is used to manage which email field is utilized and can function in many ways to meet various needs as shown in these examples:
* __'@tsdch.org'__ checks Email 1 for an address in the "tsdch.org" domain, then Email 2 if Email 1 fails, but skips the person if both fail;
* __'tsdch.org'__ functions as above, but would allow for addresses in subdomains such as "@students.tsdch.org" to be used;
* __'@'__ checks Email 1 for any address, then Email 2 if Email 1 fails, but skips the person if neither contains an address;
* __''__ causes Email 1 to be used regardless of the contents of the field.

## Veracross export files
The script expects five CSV export files from the Veracross school information system in a folder named "downloads" in the current working directory. The 'renameExports.py' script will move exported CSV files from the Downloads in the user's home directory (*if exports are located elsewhere, simply edit the variable __sourceFolder__ in 'renameExports.py'*) into the correct folder in the working directory while also striping off the information appeded to query names when downloading CSV files. The students query include weighted and unweighted gpa calculation that are not used in the code as posted here on github so you will want to uncheck those before running the query, or update the code to include gpa.  
* adminsC.csv - (*from an export Find Staff/Faculty query using a Profile Code to distinguish addmins 328516*)
* enrollmentsC.csv - (*from an export of a Find Class Enrollment Records query 325696*)
* sectionsC.csv - (*from an export of a Class Permission query 325726*)
* studentsC.csv - (*from an export of a Find Students query 328467*)
* teachersC.csv - (*from an export Find Staff/Faculty query 328480*)

The results of the script intended to be in a folder named "uploadClever" in the same folder where the script files are located. The names of the Veracross export files and the locations of both input files and output files is set in the "main" function of the script and is easily edited if needed by the individual user.

## Headers of the files for importing
The file fieldsList.py identifies the field names required in the header row of csv import files for Clever. This file is used by the script creating the files for importing and must be in the same directory as uploadClever.py when it is run. Running this file itself merely outputs a listing of all the field names to the terminal window. The output of field names does also identify which ones are required by Clever to have a successful import.

## Schools not included
The schools.csv file needs to exist, but due to its static nature it is manually creaded and placed in the uploadClever file which is the synchronized to the Clever server. I've not updated it in years, but your situation may be different.
