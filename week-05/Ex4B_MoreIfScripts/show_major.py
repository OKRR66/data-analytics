# show_major
#Create a script named show_major.py that defines two variables for a student: student_name and student_major. 
student_name = "Onur"
student_major = "HIST"
# The student_major variable will contain a code for the student’s major (e.g. ENG).

#Use the following table to create lookup logic to display the name of the major and location of the department’s office based on the major code:
majors = {
    "BIOL": {"major_name": "Biology", "office": "Science Bldg, Room 310"},
    "CSCI": {"major_name": "Computer Science", "office": "Sheppard Hall, Room 314"},
    "ENG":  {"major_name": "English", "office": "Kerr Hall, Room 201"},
    "HIST": {"major_name": "History", "office": "Kerr Hall, Room 114"},
    "MKT":  {"major_name": "Marketing", "office": "Westly Hall, Room 310"}
}

#What should your program do if a major code is not included in the table? Include an alternative to display <unknown> for the major name and nothing for location
if student_major in majors:
    major_name = majors[student_major]["major_name"]
    major_office = majors[student_major]["office"]
    print(f"{student_name}'s major is {major_name}, located at {major_office}")
else:
    print(f"{student_name}'s major is <unknown>")