#!/usr/bin/env python3
'''Field list and some functions for upload script. This file and must be
in the same folder as the uploadClever.py file for it to function.
Running this alone prints a list of all field lists in the file to the terminal.
'''


def gradesNoEmail(grade):
    emailOff = ['TK','K','1','2','3','4','5','6']
    if grade in emailOff:
        return True
    return False


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


'''Fields for Clever script
'''
def schoolsFieldsC():
    #Required: 'School_id', 'School_name', 'School_number'
    fields = ['School_id', 'School_name', 'School_number',
              'State_id','Low_grade', 'High_grade',
              'Principal', 'Principal_email', 'School_address',
              'School_city', 'School_state', 'School_zip', 'School_phone']
    return fields


def studentsFieldsC():
    #Required: 'School_id', 'Student_id',
    #          'First_name', 'Last_name'
    fields = ['School_id',
              'Student_id',
              'Student_number',
              'State_id',
              'Last_name',
              'Middle_name',
              'First_name',
              'Grade',
              'Gender',
              'Graduation_year',
              'DOB',
              'Race',
              'Hispanic_Latino',
              'Home_language',
              'Ell_status',
              'Frl_status',
              'IEP_status',
              'Student_street',
              'Student_city',
              'Student_state',
              'Student_zip',
              'Student_email',
              'Contact_relationship',
              'Contact_type',
              'Contact_name',
              'Contact_phone',
              'Contact_phone_type',
              'Contact_email',
              'Contact_sis_id',
              'Username',
              'Password',
              'Unweighted_gpa',
              'Weighted_gpa']
    return fields


def teachersFieldsC():
    #Required: 'School_id', 'Teacher_id',
    #          'First_name', 'Last_name'
    fields = ['School_id', 'Teacher_id', 'Teacher_number',
              'State_teacher_id', 'Teacher_email', 'First_name', 'Middle_name',
              'Last_name', 'Title', 'Username', 'Password']
    return fields


def adminsFieldsC():
    #Required: 'School_id', 'Staff_id', 'Admin_email'
    #          'First_name', 'Last_name'
    fields = ['School_id', 'Staff_id', 'Admin_email',
              'First_name', 'Last_name', 'Admin_title',
              'Username', 'Password', 'Role']
    return fields


def sectionsFieldsC():
    #Required: 'School_id', 'Section_id', 'Teacher_id'
    fields = ['School_id', 'Section_id', 'Teacher_id', 'Teacher_2_id',
              'Teacher_3_id', 'Teacher_4_id', 'Teacher_5_id',
              'Teacher_6_id', 'Teacher_7_id', 'Teacher_8_id',
              'Teacher_9_id', 'Teacher_10_id', 'Section_number', 'Name', 'Grade',
              'Course_name', 'Course_number', 'Course_description',
              'Period', 'Subject', 'Term_name', 'Term_start', 'Term_end']
    return fields


def enrollmentsFieldsC():
    #Required: 'School_id', 'Section_id', 'Student_id'
    fields = ['School_id', 'Section_id', 'Student_id']
    return fields


'''End of field definitions and beginning of main function that prints the
field lists to the terminal windowself.
'''
def main():
    #Prints the field list for Clever to the terminal window one per line.
    print('Clever fields Schools File:')
    print("Required: 'School_id', 'School_name', 'School_number'")
    for field in schoolsFieldsC():
        print(field)
    print()
    print('Clever fields Students File:')
    print("Required: 'School_id', 'Student_id', 'First_name', 'Last_name'")
    for field in studentsFieldsC():
        print(field)
    print()
    print('Clever fields Teachers File:')
    print("Required: 'School_id', 'Teacher_id', 'First_name', 'Last_name'")
    for field in teachersFieldsC():
        print(field)
    print()
    print('Clever fields Admins File:')
    print("Required: 'School_id', 'Staff_id', 'Admin_email', 'First_name', 'Last_name'")
    for field in adminsFieldsC():
        print(field)
    print()
    print('Clever fields Sections File:')
    print("Required: 'School_id', 'Section_id', 'Teacher_id'")
    for field in sectionsFieldsC():
        print(field)
    print()
    print('Clever fields Enrollments File:')
    print("Required: 'School_id', 'Section_id', 'Student_id'")
    for field in enrollmentsFieldsC():
        print(field)
    print()


    return

if __name__ == '__main__': main()
