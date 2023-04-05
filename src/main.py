from dicttoxml import dicttoxml
from xml.dom.minidom import parseString
import os

def main():
    student_list = []
    with open('student_list.txt', 'r') as file:
        student_list = file.readlines()
    students = []
    student_id = 1
    for s in student_list:
        parse_data = s.split()
        students.append({
            "ID": student_id,
            "NAMES": {
                "FIRST_NAME": parse_data[0],
                "SECOND_NAME": parse_data[1],
                "THIRD_NAME": parse_data[2],     
            },
            "BINDING": {
                "INFO": {
                    "COURSE": 3,
                    "FACULTY": 'ИАИТ',
                    "FACULTY-NUMBER": 5,
                },
                "ADDITIONAL_INFO": parse_data[3]    
            }
        })
        student_id += 1
    my_item_func = lambda x: x[:-1]
    xml =  dicttoxml(students, custom_root='STUDENTS', attr_type=False, item_func=my_item_func)
    
    dom = parseString(xml)
    file_name = 'student_list.xml'
    try:
        os.remove(file_name)
    except OSError as e:
        pass
    prettyfied_str: str = dom.toprettyxml()
    prettyfied_str = prettyfied_str.split('?>')
    final_dom = prettyfied_str[0] + '?>'
    final_dom += "<?xml-stylesheet type=\"text/css\" href=\"student_styles.css\"?>"
    final_dom += prettyfied_str[1]
    with open(file_name, "w") as file:
        file.write(final_dom)

if __name__ == "__main__":
    main()