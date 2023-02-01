import mysql.connector
from course import Course

database = mysql.connector.connect(
    host='ix.cs.uoregon.edu',
    port=3673,
    user='guest',
    password='guest'
)

cursor = database.cursor()
cursor.execute("USE 422json")


def list_departments():
    """
    Returns a list of the natural science courses available at the UO
    Aimed to be used by UI.
    """
    return ['PSY', 'PHYS', 'MATH', 'HPHY', 'GEOL', 'CIS', 'CH']


def list_course_levels_within_department(department):
    """
    Returns a list of x-level courses offered by a certain department.
    For example, if department input argument = 'CIS', output would be:
        ['CIS600', 'CIS500', 'CIS400', 'CIS300', 'CIS200', 'CIS100']
    Aimed to be used by UI.
    """

    query = (f"SELECT course_name\n"
             f"FROM naturalsciences\n"
             f"WHERE course_name LIKE '{department}%'")

    cursor.execute(query)
    data = cursor.fetchall()

    courses = []

    for course in data:
        course_name = course[0]  # Data from MySQL is returned via tuple. course_name is 0th index.
        course_level = ''
        for i in course_name:
            course_level += i  # Iterate through course_name until an integer is found in the string.
            if i.isdigit():  # When a digit is found, then break the loop. What's left is something like: 'MATH1' or 'CIS2'
                break
        course_level += '00'  # Then add the remaining '00' on top of 'MATH1' with final string being 'MATH100'
        if course_level not in courses:  # If course_level is not in the course list, then append to it.
            courses.append(course_level)

    return courses


def list_indiv_courses_within_department(department):
    """
    Returns a list of individual courses offered at the UO given a natural sciences department.
    For example, if department argument = 'CIS', output would be:
        ['CIS650', 'CIS640', 'CIS630', 'CIS624', 'CIS621',...]
    Aimed to be used by UI.
    """
    query = (f"SELECT course_name\n"
             f"FROM naturalsciences\n"
             f"WHERE course_name LIKE '{department}%'")

    cursor.execute(query)
    data = cursor.fetchall()

    courses = []
    for course in data:
        course_name = course[0]  # Data from MySQL is returned via tuple. course_name is 0th index.
        if course_name not in courses:  # If course not already in course list then append to it.
            courses.append(course_name)

    return courses


def search(data):
    names = {}

    for course in data:
        name = course[2]
        aperc = course[3]
        bperc = course[4]
        cperc = course[5]
        dperc = course[6]
        fperc = course[7]
        if name not in names:
            names[name] = Course(name, aperc, bperc, cperc, dperc, fperc)
        else:
            names[name].adjust_percentages(aperc, bperc, cperc, dperc, fperc)

    return list(names.values())


def search_by_instructor(course):
    """
    Breaks down professor grade distributions by the following depending on the following inputs:
        1.) A single class (such as 'MATH 111')
        2.) A single department (such as 'MATH')
        3.) All classes of a particular level within a department (such as 'Math 100-level' classes)

    Returns a list of professor classes with names and corresponding grade distributions as members.
    """
    query = (f"SELECT *\n"
             f"FROM naturalsciences\n"
             f"WHERE COURSE_NAME = '{course}'")
    cursor.execute(query)
    data = cursor.fetchall()

    return search(data)


def search_by_department_level(dep_level):
    """
    Breaks down grade distribution by a particular level within a department.
    Examples of valid inputs are: 'MATH400', 'CIS100', 'CH200'

    Returns a list of classes consisting of courses and their corresponding grade distributions as members.
    """
    query = (f"SELECT *\n"
             f"FROM naturalsciences\n"
             f"WHERE ")


print(list_indiv_courses_within_department('CIS'))
