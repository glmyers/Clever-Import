#!/usr/bin/env python3
'''Field lists for all import script upload files and must be
in the same folder as the uploadName.py file for it to function.
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


def calendarFieldsVC():
    fields =['description',
            'event_type',
            'school_level',
            'grade_level',
            'public_calendar',
            'parent_calendar',
            'student_calendar',
            'staff_faculty_calendar',
            'alumni_calendar',
            'group_members_calendar',
            'primary_groups',
            'start_date',
            'end_date',
            'start_time',
            'end_time',
            'leave_class_time',
            'leave_campus',
            'return_to_campus',
            'notes',
            'resource_id',
            'campus',
            'contact_person_id',
            'security_notes',
            'cleaning_notes',
            'maintenance_notes',
            'catering_notes',
            'av_notes']
    return fields


'''Fields for Seesawr script
'''
def seesawFields():
    #Required: 'location_id', 'location_name'
    fields = ['Teacher Email', 'Teacher First Name', 'Teacher Last Name',
                'Class Name', 'Grade Level', 'Sign In Mode', 'Student Name',
                'Student ID', 'Student Email', 'Student Password',
                'Co-Teacher 1 Email', 'Co-Teacher 1 First Name', 'Co-Teacher 1 Last Name',
                'Co-Teacher 2 Email', 'Co-Teacher 2 First Name', 'Co-Teacher 2 Last Name',
                'Co-Teacher 3 Email', 'Co-Teacher 3 First Name', 'Co-Teacher 3 Last Name',
                'Co-Teacher 4 Email', 'Co-Teacher 4 First Name', 'Co-Teacher 4 Last Name',
                'Co-Teacher 5 Email', 'Co-Teacher 5 First Name', 'Co-Teacher 5 Last Name']
    return fields


'''Fields for Apple School Manager script
'''
def locationFields():
    #Required: 'location_id', 'location_name'
    fields = ['location_id', 'location_name']
    return fields


def studentsFields():
    #Required: 'person_id', 'first_name', 'last_name', 'location_id'
    fields = ['person_id', 'person_number',
                'first_name', 'middle_name', 'last_name',
                'grade_level', 'email_address', 'sis_username',
                'password_policy',
                'location_id']
    return fields


def staffFields():
    #Required: 'person_id', 'first_name', 'last_name', 'location_id'
    fields = ['person_id', 'person_number',
                'first_name', 'middle_name', 'last_name',
                'email_address', 'sis_username',
                'location_id', 'location_id_2', 'location_id_3',
                'location_id_4', 'location_id_5', 'location_id_6',
                'location_id_7', 'location_id_8', 'location_id_9',
                'location_id_10', 'location_id_11', 'location_id_12',
                'location_id_13', 'location_id_14', 'location_id_15']
    return fields


def coursesFields():
    #Required: 'course_id', 'location_id'
    fields = ['course_id', 'course_number', 'course_name',
                'location_id']
    return fields


def classesFields():
    #Required: 'class_id', 'course_id', 'location_id'
    fields = ['class_id', 'class_number', 'course_id',
                'instructor_id', 'instructor_id_2', 'instructor_id_3',
                'instructor_id_4', 'instructor_id_5', 'instructor_id_6',
                'instructor_id_7', 'instructor_id_8', 'instructor_id_9',
                'instructor_id_10', 'instructor_id_11', 'instructor_id_12',
                'instructor_id_13', 'instructor_id_14', 'instructor_id_15',
                'location_id']
    return fields


def rostersFields():
    #Required: 'roster_id', 'class_id', 'student_id'
    fields = ['roster_id', 'class_id', 'student_id']
    return fields


'''Fields for Create Emails script
'''
def contactFields():
    fields = ['person_fk',
                'email_1',
                'email_2',
                'phone_home',
                'phone_mobile',
                'phone_business']
    return fields


def emailFields():
    fields = ['PersonID', 'Email', 'First', 'Last', 'Assigned', 'Level', 'Year']
    return fields


'''Fields for IMS script
'''
def orgsFieldsIMS():
    #Required: 'sourcedId', 'name', 'type'
    fields = ['sourcedId', 'status', 'dateLastModified', 'name',
              'type', 'identifier', 'metadata.classification',
              'metadata.gender', 'metadata.boarding', 'parentSourcedId']
    return fields


def usersFieldsIMS():
    #Required: 'sourcedId', 'orgSourcedIds', 'role', 'username',
    #          'givenName', 'familyName'
    fields = ['sourcedId', 'status', 'dateLastModified',
              'orgSourcedIds', 'role', 'username',
              'userId', 'givenName', 'familyName',
              'identifier', 'email', 'sms', 'phone',
              'agents']
    return fields


def coursesFieldsIMS():
    #Required: 'sourcedId', 'title'
    fields = ['sourcedId', 'status', 'dateLastModified', 'schoolYearId',
              'metadata.duration', 'title', 'courseCode', 'grade',
              'orgSourcedId', 'subjects']
    return fields


def classesFieldsIMS():
    #Required: 'sourcedId', 'title', 'classType', 'schoolSourcedId', 'termSourcedId'
    fields = ['sourcedId', 'status', 'dateLastModified', 'title', 'grade',
              'courseSourcedId', 'classCode', 'classType', 'location',
              'schoolSourcedId', 'termSourcedId', 'subjects']
    return fields


def enrollmentsFieldsIMS():
    #Required: 'sourcedId', 'classSourcedId', 'schoolSourcedId', 'userSourcedId', 'role'
    fields = ['sourcedId', 'classSourcedId', 'schoolSourcedId', 'userSourcedId',
              'role', 'status', 'dateLastModified', 'primary']
    return fields


def academicSessionsFieldsIMS():
    #Required: 'sourcedId', 'title', 'type', 'startDate', 'endDate'
    fields = ['sourcedId', 'status', 'dateLastModified', 'title', 'type',
              'startDate', 'endDate', 'parentSourcedId']
    return fields


def demographicsFieldsIMS():
    #Required: 'userSourcedId', 'birthdate', 'sex',
    #          'americanIndianOrAlaskaNative', 'asian',
    #          'blackOrAfricanAmerican', 'nativeHawaiianOrOtherPacificIslander',
    #          'white', 'demographicRaceTwoOrMoreRaces', 'hispanicOrLatinoEthnicity',
    #          'countryOfBirthCode', 'stateOfBirthAbbreviation', 'cityOfBirth',
    #          'publicSchoolResidenceStatus'
    fields = ['userSourcedId', 'status', 'dateLastModified', 'birthdate', 'sex',
              'americanIndianOrAlaskaNative', 'asian', 'blackOrAfricanAmerican',
              'nativeHawaiianOrOtherPacificIslander', 'white',
              'demographicRaceTwoOrMoreRaces', 'hispanicOrLatinoEthnicity',
              'countryOfBirthCode', 'stateOfBirthAbbreviation', 'cityOfBirth',
              'publicSchoolResidenceStatus']
    return fields


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


'''Fields for Schoology script
'''
def coursesFieldsS():
    #Required:
    fields = ['Course Name', 'Department Name', 'Course Code', 'Credits',
              'Course Description', 'Section Name', 'Section School Code',
              'Section Code', 'Section Description', 'Location',
              'School Building', 'Grading Periods']
    return fields


def enrollmentsFieldsS():
    #Required
    fields = ['Course Code', 'Section Code', 'Section School Code',
              'User Unique ID', 'Enrollment Type', 'Grading Periods']
    return fields


def usersFieldsS():
    #Required
    fields = ['First Name', 'First Name (Preferred)', 'Middle Name', 'Last Name',
              'Name Prefix', 'Username', 'E-mail', 'Unique User ID', 'Role',
              'School', 'Schoology User ID', 'Position/Job Title', 'Password',
              'Gender', 'Grad Year', 'Additional Schools']
    return fields


def destinyFields():
    #Fields utilized
    fields = ['SiteShortName',
            'Barcode',
            'DistrictID',
            'LastName',
            'FirstName',
            'MiddleName',
            'Nickname',
            'PatronType',
            'AccessLevel',
            'Status',
            'Gender',
            'Homeroom',
            'GradeLevel',
            'IsTeacher',
            'GraduationYear',
            'Birthdate',
            'Username',
            'EmailPrimary']
    return fields


'''End of field definitions and beginning of main function that prints the
field lists to the terminal windowself.
'''
def main():
    #Prints the Destiny field list to the terminal window one per line.
    print()
    print('Destiny field list:')
    for field in destinyFields():
        print(field)
    print()
    print()

    #Prints the Seesaw field list to the terminal window one per line.
    print()
    print('Seesaw field list:')
    for field in seesawFields():
        print(field)
    print()
    print()

    #Prints the field list for Apple School Manager to the terminal window one per line.
    print('ASM fields Location File:')
    print("Required: 'location_id', 'location_name'")
    for field in locationFields():
        print(field)
    print()
    print('ASM fields Students File:')
    print("Required: 'person_id', 'first_name', 'last_name', 'location_id'")
    for field in studentsFields():
        print(field)
    print()
    print('ASM fields Staff File:')
    print("Required: 'person_id', 'first_name', 'last_name', 'location_id'")
    for field in staffFields():
        print(field)
    print()
    print('ASM fields Courses File:')
    print("Required: 'course_id', 'location_id'")
    for field in coursesFields():
        print(field)
    print()
    print('ASM fields Classes File:')
    print("Required: 'roster_id', 'course_id', 'location_id'")
    for field in classesFields():
        print(field)
    print()
    print('ASM fields Rosters File:')
    print("Required: 'class_id', 'class_id', 'student_id'")
    for field in rostersFields():
        print(field)
    print()

    #Prints the field list for New Student Emails to the terminal window one per line.
    print()
    print('New Student Emails field list:')
    for field in contactFields():
        print(field)
    print()

    #Prints the IMS field list to the terminal window one per line.
    print()
    print('IMS orgs.csv field list:')
    print("Required: 'sourcedId', 'name', 'type'")
    for field in orgsFields():
        print(field)
    print()
    print('IMS users.csv field list:')
    print("Required: 'sourcedId', 'orgSourcedIds', 'role', 'username', 'givenName', 'familyName'")
    for field in usersFields():
        print(field)
    print()
    print('IMS courses.csv field list:')
    print("Required: 'sourcedId', 'title'")
    for field in coursesFields():
        print(field)
    print()
    print('IMS classes.csv field list:')
    print("Required: 'sourcedId', 'title', 'classType', 'schoolSourcedId', 'termSourcedId'")
    for field in classesFields():
        print(field)
    print()
    print('IMS enrollments.csv field list:')
    print("Required: 'sourcedId', 'classSourcedId', 'schoolSourcedId', 'userSourcedId', 'role'")
    for field in enrollmentsFields():
        print(field)
    print()
    print('IMS academicSessions.csv field list:')
    print("Required: 'sourcedId', 'title', 'type', 'startDate', 'endDate'")
    for field in academicSessionsFields():
        print(field)
    print()
    print('IMS demographics.csv field list:')
    print("Required: 'userSourcedId', 'birthdate', 'sex', 'americanIndianOrAlaskaNative', 'asian', 'blackOrAfricanAmerican', 'nativeHawaiianOrOtherPacificIslander', 'white', 'demographicRaceTwoOrMoreRaces', 'hispanicOrLatinoEthnicity', 'countryOfBirthCode', 'stateOfBirthAbbreviation', 'cityOfBirth', 'publicSchoolResidenceStatus'")
    for field in demographicsFields():
        print(field)
    print()

    #Prints field list for uploadSchoology
    print()
    print('Schoology fields')
    Print()
    print('courses.csv field list')
    for field in coursesFieldsS():
        print(field)
    print()
    print('enrolments.csv field list')
    for field in enrollmentsFieldsS():
        print(field)
    print()
    print('users.csv field list')
    for field in usersFieldsS():
        print(field)
    print()

    return

if __name__ == '__main__': main()
