#Build a class Employee with multiple constructors that can initialize an employee object in different ways.

class Employee:
    def __init__(self, name, age, department):
        self.name= name
        self.age= age
        self.department= department
    @classmethod
    def from_string(cls, employee_string):
        name, age, department= employee_string.split("-")
        return cls(name, int(age), department)
    @classmethod
    def from_dictionary(cls, employee_dictionary):
        return cls(employee_dictionary["name"], employee_dictionary["age"], employee_dictionary["department"])
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Department: {self.department}") 

employee1= Employee("Francis", 26, "Sales")
employee2= Employee("Vincent", 24, "IT")
employee3= Employee("Sara", 21, "HR")

employee1.display()
employee2.display()
employee3.display()
