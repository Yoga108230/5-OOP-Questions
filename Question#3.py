#Build a two class call SchoolOne and SchoolTwo that display there list of students average grades and GPA.

class School:
    def __init__(self, name, students):
        self.name= name
        self.students= students
    def calculate_gpa(self, grades):
        average= sum(grades)/ len(grades)
        if average>= 98.51:
            return 4.0
        elif average>= 96.51:
            return 3.75
        elif average>= 94.51:
            return 3.50
        elif average>= 92.51:
            return 3.25
        elif average>= 90.51:
            return 3.00
        elif average>= 88.51:
            return 2.75
        elif average>= 86.51:
            return 2.50
        elif average>= 84.51:
            return 2.25
        elif average>= 82.51:
            return 2.00
        elif average>= 80.51:
            return 1.75
        elif average>= 78.51:
            return 1.50
        elif average>= 76.51:
            return 1.25
        elif average>= 74.51:
            return 1.00
        elif average<= 74.50:
            return 0.00
    def display_students(self):
        print(f"{self.name} Student Records:")
        for student in self.students:
            average_grade= sum(student['grades'])/ len(student['grades'])
            gpa= self.calculate_gpa(student['grades'])
            print(f"Student: {student['name']}, Average Grade: {average_grade:.2f}, GPA: {gpa:.1f}")

class SchoolOne(School):
    pass

class SchoolTwo(School):
    pass

students_one= [{'name': "Vincent", 'grades': [80, 80]}, {'name': "Francis", 'grades': [90, 95]}]
students_two= [{'name': "Sara", 'grades': [85, 90]}, {'name': "Carmel", 'grades': [95, 95]}]

school_one= SchoolOne("School One", students_one)
school_two= SchoolTwo("School Two", students_two)

school_one.display_students()
school_two.display_students()
