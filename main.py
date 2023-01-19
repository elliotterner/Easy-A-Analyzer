import json

json_data = open("gradedata.json", "r")
grade_data = json.load(json_data)

def list_courses():
    """Returns a list of all courses offered.
    Can be used for a dropdown menu in the UI."""
    return [course for course in grade_data]

def list_departments():
    """Returns a list of departments at the UO.
    Can be used for a dropdown menu in the UI."""
    departments = []
    for course in grade_data:
        course_without_number = ''.join([i for i in course if not i.isdigit()])
        if course_without_number not in departments:
            departments.append(course_without_number)

    return departments

def list_data_single_course(course):
    """Takes a course as input and outputs the professor and grade percentage distribution for each term"""
    return grade_data[course]

list_departments()