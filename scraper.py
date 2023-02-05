from bs4 import BeautifulSoup
import mysql.connector
import requests
import re


def get_department_links():
    url = 'https://web.archive.org/web/20140901091007/http://catalog.uoregon.edu/arts_sciences/'
    request = requests.get(url)

    raw_html_text = request.text
    processed_html_text = BeautifulSoup(raw_html_text, 'html.parser')

    department_links = []

    for line in processed_html_text.find_all(id="/arts_sciences/"):
        html_line = str(line)  # fix
        domain = 'https://web.archive.org'
        subdirectories = re.findall('"([^"]*)"', html_line)
        for i in range(2, len(subdirectories)):
            subdirectory = subdirectories[i]
            department_links.append(domain + subdirectory)

    return department_links


def get_faculty_members(department_link):
    request = requests.get(department_link)
    raw_html_text = request.text
    processed_html_text = BeautifulSoup(raw_html_text, 'html.parser')

    instructor_names = []

    for line in processed_html_text.find_all(id="facultytextcontainer"):
        html_lines = line.text.split("\n")
        for instructor_and_department in html_lines:

            if instructor_and_department.find("Clark, Jessie H.") > -1:
                instructor_names.append("Jessie H Clark")
                continue

            comma_index = instructor_and_department.find(",")
            if comma_index > -1:
                instructor_name = instructor_and_department[0:comma_index]
                instructor_name = re.sub(r'\"[^)]*\"', '', instructor_name)
                instructor_name = re.sub(r'\([^)]*\)', '', instructor_name)
                instructor_name = re.sub(' [A-Z]. ', ' ', instructor_name)
                instructor_name = re.sub(' [A-Z]. ', ' ', instructor_name)
                instructor_name = re.sub('[.]', '', instructor_name)
                instructor_name = re.sub(' +', ' ', instructor_name)
                instructor_names.append(instructor_name)

    return instructor_names


def parse_instructor_name(instructor_name):
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
    parsed_name = [i for i in parsed_name if i]
    # if len(parsed_name[0]) == 1 or len(parsed_name[1]) == 1:
    # parsed_name[:2] = [' '.join(parsed_name[:2])]
    if (parsed_name[len(parsed_name) - 1]) == "Jr" or (parsed_name[len(parsed_name) - 1]) == "Sr" or (
            parsed_name[len(parsed_name) - 1]) == "II":
        parsed_name[1:3] = [' '.join(parsed_name[1:3])]

    return parsed_name


def mysql_filter(parsed_name):
    database = mysql.connector.connect(host="ix.cs.uoregon.edu", port=3673, user="prodrig2", password="irodmario@2001",
                                       database="422json")
    cursor = database.cursor()

    cursor.execute("SET SQL_SAFE_UPDATES = 0")
    query = (f"UPDATE gradedata\n"
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