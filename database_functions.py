import mysql.connector
from professor import Professor

database = mysql.connector.connect(
    host='ix.cs.uoregon.edu',
    port=3673,
    user='guest',
    password='guest'
)

cursor = database.cursor()
cursor.execute("USE 422json")

def data_single_course(course):
    query = (f"SELECT *\n"
             f"FROM naturalsciences\n"
             f"WHERE COURSE_NAME = '{course}'")
    cursor.execute(query)

    data = cursor.fetchall()

    instructors = {}

    for course in data:
        course_name = course[0]
        instructor = course[2]
        aperc = course[3]
        bperc = course[4]
        cperc = course[5]
        dperc = course[6]
        fperc = course[7]
        if instructor not in instructors:
            instructors[instructor] = Professor(instructor, course_name, aperc, bperc, cperc, dperc, fperc)
        else:
            instructors[instructor].adjust_percentages(aperc, bperc, cperc, dperc, fperc)

    print(list(instructors.values()))

data_single_course("MATH111")