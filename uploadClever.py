#!/usr/bin/env python3
'''Creates the import files for Clever using CSV exports from
Veracross. The file fieldList.py containing
the export file field names must be in the same folder as this program.

Import file names are set in the main function and the path of their location
is set using the 'inputs' variable.

Export file names should not be altered since Clever is expecting specific
file names. The path of their location is set using the 'results' variable.

****DO NOT CHANGE THE NAMES OF THE RESULT FILES.****
'''

#Import code desired from the standard library.
import csv
from sys import argv
from pathlib import Path
from getpass import getuser
from collections import defaultdict
#Function to rename and move Veracross CSV exports.
from renameExports import vcxFiles
#Import the fieldnames for the export files.
from fieldList import studentsFieldsC as fstudents
from fieldList import teachersFieldsC as fteachers
from fieldList import adminsFieldsC as fadmins
from fieldList import sectionsFieldsC as fsections
from fieldList import enrollmentsFieldsC as fenrollments
from fieldList import schoolsFieldsC as fschools
#Domain for school email system
domain = '@tsdch.org'
# List of Person IDs of students who temporaroly are without parents..
noParents = ['']
# List of Person IDs of teachers with role "Other" that actually teach the class.
multiTeacher = ['']


def schoolLevels():
    schoolsDict = {'Lower School':'LS','Middle School':'MS', 'Upper School':'US', \
    'All School':'AS'}
    return schoolsDict


def gradeLevels():
    gradesDict = {'Grade 12':12, 'Grade 11':11, 'Grade 10':10, 'Grade 9':9, \
    'Grade 8':8, 'Grade 7':7, 'Grade 6':6, 'Grade 5':5, 'Grade 4':4, \
    'Grade 3':3, 'Grade 2':2, 'Grade 1':1, 'TK':'Prekindergarten', \
    'Kindergarten':'Kindergarten'}
    return gradesDict

'''
def createSchools(inFile, outFile, divisions, gradeNumber):
    with open(inFile, 'r') as dataIn, open(outFile, 'w') as dataOut:
        reader = csv.DictReader(dataIn)
        writer = csv.DictWriter(dataOut, fieldnames=fschools(),
                                quoting=csv.QUOTE_MINIMAL)
        #Put the header row of fields at the top of the output file.
        writer.writeheader()
    return
'''

def createStudents(inFile, outFile, divisions, gradeNumber):
    #Create a CSV export file by processing the existing data files.
    with open(inFile, 'r') as dataIn, open(outFile, 'w') as dataOut:
        reader = csv.DictReader(dataIn)
        writer = csv.DictWriter(dataOut, fieldnames=fstudents(),
                                quoting=csv.QUOTE_ALL)
        #Put the header row of fields at the top of the output file.
        writer.writeheader()
        #Output data to the file for all users.
        for row in reader:
            # Confirm student email is in the school domain
            if domain in row['Email 1']:
                sEmail = row['Email 1']
            elif domain in row['Email 2']:
                sEmail = row['Email 2']
            else:
                continue
            x = 0
            while x < 4:
                x += 1
                if row[f'Parent {x} Relationship'] == '':
                    if row['Person ID'] in noParents:
                        x = 4
                    else:
                        break
                new = defaultdict(dict)
                new['School_id'] = divisions[row['School Level']]
                new['Student_id'] = row['Person ID']
                new['Student_number'] = row['Person ID']
                new['State_id'] = ''
                new['Last_name'] = row['Last Name']
                new['Middle_name'] = row['Middle Name']
                new['First_name'] = row['First Nick Name']
                new['Grade'] = gradeNumber[row['Current Grade']]
                new['Gender'] = row['Gender']
                new['Graduation_year'] = row['Graduation Year']
                new['DOB'] = row['Birthday']
                new['Race'] = ''
                new['Hispanic_Latino'] = ''
                new['Home_language'] = ''
                new['Ell_status'] = ''
                new['Frl_status'] = ''
                new['IEP_status'] = ''
                new['Student_street'] = row['Address 1']
                new['Student_city'] = row['City']
                new['Student_state'] = row['State']
                new['Student_zip'] = row['Zip (5-digit)']
                new['Student_email'] = sEmail
                new['Contact_relationship'] = row[f'Parent {x} Relationship']
                new['Contact_type'] = 'Family'
                new['Contact_name'] = f"{row[f'PARENT {x}: First Nick Name']} {row[f'PARENT {x}: Last Name']}"
                new['Contact_phone'] = row[f'PARENT {x}: Mobile Phone']
                new['Contact_phone_type'] = 'Cell'
                new['Contact_email'] = row[f'PARENT {x}: Email 1']
                new['Contact_sis_id'] = row[f'PARENT {x}: Person ID']
                new['Username'] = ''
                new['Password'] = ''
                new['Unweighted_gpa'] = ''
                new['Weighted_gpa'] = ''
                writer.writerow(new)
    return


def createTeachers(inFile, outFile, divisions, gradeNumber):
    #Create a CSV export file by processing the existing data files.
    with open(inFile, 'r') as dataIn, open(outFile, 'w') as dataOut:
        reader = csv.DictReader(dataIn)
        writer = csv.DictWriter(dataOut, fieldnames=fteachers(),
                                quoting=csv.QUOTE_ALL)
        #Put the header row of fields at the top of the output file.
        writer.writeheader()
        #Output data to the file for all users.
        staffDict = {}
        for row in reader:
            # Confirm teacher email is in the school domain
            if domain in row['Email 1']:
                sEmail = row['Email 1']
            elif domain in row['Email 2']:
                sEmail = row['Email 2']
            else:
                continue
            new = defaultdict(dict)
            new['School_id'] = divisions[row['School Level']]
            new['Teacher_id'] = row['Person ID']
            new['Teacher_number'] = row['Person ID']
            new['State_teacher_id'] = ''
            new['Teacher_email'] = sEmail
            new['First_name'] = row['First Nick Name']
            new['Middle_name'] = row['Middle Name']
            new['Last_name'] = row['Last Name']
            new['Title'] = row['Job Title']
            new['Username'] = ''
            new['Password'] = ''
            writer.writerow(new)
    return


def createAdmins(inFile, outFile, divisions, gradeNumber):
    #Create a CSV export file by processing the existing data files.
    with open(inFile, 'r') as dataIn, open(outFile, 'w') as dataOut:
        reader = csv.DictReader(dataIn)
        writer = csv.DictWriter(dataOut, fieldnames=fadmins(),
                                quoting=csv.QUOTE_ALL)
        #Put the header row of fields at the top of the output file.
        writer.writeheader()
        #Output data to the file for all users.
        for row in reader:
            # Confirm teacher email is in the school domain
            if domain in row['Email 1']:
                sEmail = row['Email 1']
            elif domain in row['Email 2']:
                sEmail = row['Email 2']
            else:
                continue
            new = defaultdict(dict)
            new['School_id'] = divisions[row['School Level']]
            new['Staff_id'] = row['Person ID']
            new['Admin_email'] = sEmail
            new['First_name'] = row['First Nick Name']
            new['Last_name'] = row['Last Name']
            new['Admin_title'] = row['Job Title']
            new['Username'] = ''
            new['Password'] = ''
            new['Role'] = row['Profile Code']
            writer.writerow(new)
    return


def createSections(inFile, outFile, divisions, gradeNumber):
    #Create a CSV export file by processing the existing data files.
    with open(inFile, 'r') as dataIn, open(outFile, 'w') as dataOut:
        reader = csv.DictReader(dataIn)
        writer = csv.DictWriter(dataOut, fieldnames=fsections(),
                                quoting=csv.QUOTE_ALL)
        #Put the header row of fields at the top of the output file.
        writer.writeheader()
        #Output data to the file for all users.
        classesDict = dict()
        for row in reader:
            # do not include those with role of 'Other'
            if row['Person ID'] not in multiTeacher:
                if row['Role'] == 'Other': continue
            # Roles Primary Teacher, Additional Teacher, and Teacher's Aide
            if row['Internal Class ID'] not in classesDict:
                new = defaultdict(dict)
                new['School_id'] = divisions[row['School Level']]
                new['Section_id'] = row['Internal Class ID']
                new['Teacher_id'] = row['Person ID']
                new['Name'] = f"{row['Class Name'][row['Class Name'].find(' ')+1:]}"
                new['Section_number'] = row['Class ID']
                try:
                    new['Grade'] = gradeNumber[row['Primary Grade Level']]
                except:
                    new['Grade'] = ''
                new['Course_name'] = row['Course']
                new['Course_number'] = row['Internal Course ID']
                new['Course_description']= row['Description']
                if row['Block'] == '<None Specified>':
                    period = row['Class ID']
                else:
                    period = row['Block']
                new['Period'] = period
                new['Subject'] = row['Subject']
                new['Term_name'] = ''
                new['Term_start'] = ''
                new['Term_end'] = ''
                classesDict[row['Internal Class ID']] = new
            else:
                if row['Role'] == 'Primary Teacher':
                    newTeacher = classesDict[row['Internal Class ID']]['Teacher_id']
                    classesDict[row['Internal Class ID']]['Teacher_id'] = row['Person ID']
                else:
                    newTeacher = row['Person ID']
                count = 1
                while count < 10:
                    count += 1
                    if not (classesDict[row['Internal Class ID']]
                            [f'Teacher_{count}_id'] == {}):
                        continue
                    else:
                        classesDict[row['Internal Class ID']]\
                                [f'Teacher_{count}_id'] = \
                                    newTeacher
                        break
        for ID, classes in classesDict.items():
            writer.writerow(classes)
    return


def createEnrollments(inFile, outFile, divisions, gradeNumber):
    #Create a CSV export file by processing the existing data files.
    with open(inFile, 'r') as dataIn, open(outFile, 'w') as dataOut:
        reader = csv.DictReader(dataIn)
        writer = csv.DictWriter(dataOut, fieldnames=fenrollments(),
                                quoting=csv.QUOTE_ALL)
        #Put the header row of fields at the top of the output file.
        writer.writeheader()
        for row in reader:
            new = defaultdict(dict)
            new['School_id'] = divisions[row['School Level']]
            new['Section_id'] = row['Internal Class ID']
            new['Student_id'] = row['Person ID']
            writer.writerow(new)
    return


def main():
    vcxFiles()
    print()
    inputs = Path(f'downloads')
    results = Path('uploadClever')
    abrvSchool = schoolLevels()
    abrvGrade = gradeLevels()
    #Export files from Veracross in CSV format, UTF-8
    sourceSchools = f'{inputs}/schoolsC.csv'
    sourceStudents = f'{inputs}/studentsC.csv'
    sourceTeachers = f'{inputs}/teachersC.csv'
    sourceAdmins = f'{inputs}/adminsC.csv'
    sourceSections = f'{inputs}/sectionsC.csv'
    sourceRosters = f'{inputs}/enrollmentsC.csv'
    #CSV files for upload into Clever
    resultSchools = f'{results}/schoolsTest.csv'
    resultStudents = f'{results}/students.csv'
    resultTeachers = f'{results}/teachers.csv'
    resultAdmins = f'{results}/admins.csv'
    resultSections = f'{results}/sections.csv'
    resultEnrollments = f'{results}/enrollments.csv'
    #Run functions to create the files
    #createSchools(sourceSchools,resultSchools,abrvSchool,abrvGrade)
    createStudents(sourceStudents, resultStudents, abrvSchool, abrvGrade)
    createTeachers(sourceTeachers, resultTeachers, abrvSchool, abrvGrade)
    createAdmins(sourceAdmins, resultAdmins, abrvSchool, abrvGrade)
    createSections(sourceSections, resultSections, abrvSchool, abrvGrade)
    createEnrollments(sourceRosters, resultEnrollments, abrvSchool, abrvGrade)
    print('Files are complete.')
    print()
    return


if __name__ == '__main__': main()

