"""
File Name: scraper.py
Program Name: Easy A
File purpose: This file traverses through the department links found at
    https://web.archive.org/web/20140901091007/http://catalog.uoregon.edu/arts_sciences/
    and grabs a list of faculty names. Each faculty member is then searched for in the MySQL
    database to check if they have instructed any courses found in the database. If found, then
    the "FACULTY" column to the corresponding data entry is set to "FACULTY"
Creation date: Feb 3, 2023
Initial Authors: Patrick Rodriguez
"""

from bs4 import BeautifulSoup
import mysql.connector
import requests
import re


def get_department_links():
    """
    Traverses through https://web.archive.org/web/20140901091007/http://catalog.uoregon.edu/arts_sciences/
    and returns the links to each department.
    """
    url = 'https://web.archive.org/web/20140901091007/http://catalog.uoregon.edu/arts_sciences/'
    request = requests.get(url)

    raw_html_text = request.text
    processed_html_text = BeautifulSoup(raw_html_text, 'html.parser')

    department_links = []

    for line in processed_html_text.find_all(
            id="/arts_sciences/"):  # All departments subdirectories are found in id="/arts_sciences/"
        html_line = str(line)
        domain = 'https://web.archive.org'
        subdirectories = re.findall('"([^"]*)"', html_line)  # Filter out only the subdirectory in each html line.
        for i in range(2, len(subdirectories)):  # First two lines do not contain any subdirectories so start at index 2
            subdirectory = subdirectories[i]
            department_links.append(domain + subdirectory)  # domain + subdirectory gives a valid link to a department.

    return department_links


def get_faculty_members(department_link):
    """
    Returns the faculty members of a department given a valid UO faculty link.
    """
    request = requests.get(department_link)
    raw_html_text = request.text
    processed_html_text = BeautifulSoup(raw_html_text, 'html.parser')

    instructor_names = []

    for line in processed_html_text.find_all(id="facultytextcontainer"):  # All faculty found in id="facultytextcontainer"
        html_lines = line.text.split("\n")
        for instructor_and_department in html_lines:
            if instructor_and_department.find("Clark, Jessie H.") > -1:  # Weird edge case. Only name that's formatted like this.
                instructor_names.append("Jessie H Clark")
                continue

            comma_index = instructor_and_department.find(",")  # Remove the department from the html line, leaving only names.
            if comma_index > -1:
                instructor_name = instructor_and_department[0:comma_index]
                instructor_name = re.sub(r'\"[^)]*\"', '', instructor_name)  # Nickname edge case
                instructor_name = re.sub(r'\([^)]*\)', '', instructor_name)  # Also nickname edge case
                instructor_name = re.sub(' [A-Z]. ', ' ', instructor_name)  # Any first name initials
                instructor_name = re.sub(' [A-Z]. ', ' ', instructor_name)  # Any middle name initials
                instructor_name = re.sub('[.]', '', instructor_name)
                instructor_name = re.sub(' +', ' ', instructor_name)  # Remove any white space
                instructor_names.append(instructor_name)

    return instructor_names


def parse_instructor_name(instructor_name):
    """
    Parses an instructor string into a list of separated subnames.
    """
    '''These if statements tackle unusual name edge cases'''
    if instructor_name == "Peter von Hippel":
        return ["Peter", "von Hippel"]
    if instructor_name == "Donald Van Houten":
        return ["Donald", "Van Houten"]
    if instructor_name == "Anne van den Nouweland":
        return ["Anne", "van den Nouweland"]
    if instructor_name == "Steven van Enk":
        return ["Steven", "van Enk"]
    if instructor_name == "Kathleen Freeman Hennessy":
        return ["Kathleen", "Freeman Hennessy"]
    if instructor_name == "W Whitelaw":
        return ["W Ed", "Whitelaw"]
    if instructor_name == "G Brown":
        return ["G", "Brown"]
    if instructor_name == 'T Givón':
        return ["T", "Givón"]
    if instructor_name == "J Sanders":
        return ["J", "Sanders"]

    parsed_name = instructor_name.split(" ")
    parsed_name = [i for i in parsed_name if i]  # Removes any list entries containing an empty string.

    '''This accounts for any suffixes found in a person's last name'''
    if (parsed_name[len(parsed_name) - 1]) == "Jr" or (parsed_name[len(parsed_name) - 1]) == "Sr" or (
            parsed_name[len(parsed_name) - 1]) == "II":
        parsed_name[1:3] = [' '.join(parsed_name[1:3])]

    return parsed_name


def mysql_filter(parsed_name):
    """
    Given a list of subnames joined together to create a faculty member's name, search the MySQL
    database for any courses taught by this faculty member. If found, then set the data entry's FACULTY column
    to "FACULTY"
    """
    database = mysql.connector.connect(host="ix.cs.uoregon.edu", port=3673, user="prodrig2", password="irodmario@2001",
                                       database="422json")
    cursor = database.cursor()

    cursor.execute("SET SQL_SAFE_UPDATES = 0")
    query = (f"UPDATE naturalsciences\n"  # change
             f"SET faculty = 'FACULTY'\n")

    last_name_index = len(parsed_name) - 1
    last_name = parsed_name[last_name_index]
    mysql_where = f"WHERE instructor LIKE '{last_name}, "

    for i in range(last_name_index):
        mysql_where += f"%{parsed_name[i]}% "

    query += mysql_where
    query = query[:-1]
    query += "';"

    cursor.execute(query)
    cursor.execute("SET SQL_SAFE_UPDATES = 1")
    database.commit()
    database.close()


def scrape():
    """
    The finished scraper. It combines all functions defined above to traverse through the entire web archive URL
    and modify any courses taught by faculty members.
    """
    department_links = get_department_links()
    for department_link in department_links:
        faculty_list = get_faculty_members(department_link)
        parsed_faculty_names = []
        for faculties in faculty_list:
            parsed_faculty_names.append(parse_instructor_name(faculties))
            for faculty in parsed_faculty_names:
                mysql_filter(faculty)


if __name__ == '__main__':
    scrape()
