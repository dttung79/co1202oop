# Create a class called Student that has the following attributes:
# - id
# - name
# - gpa
# Methods:
# + __init__(self, id, name, gpa): constructor
# + show(self): display the student's information
# get/set methods for name and gpa
# get for id

class Student:
    def __init__(self, id, name, gpa):
        self.__id = id
        self.__name = name
        self.__gpa = gpa
    
    def show(self):
        print(f"ID: {self.__id}\nName: {self.__name}\nGPA: {self.__gpa}")
    
    def get_id(self):
        return self.__id
    
    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        if name != "":
            self.__name = name
        else:
            print("Student name cannot be empty")
    
    def get_gpa(self):
        return self.__gpa
    
    def set_gpa(self, gpa):
        if gpa >= 0 and gpa <= 4:
            self.__gpa = gpa
        else:
            print("GPA must be between 0 and 4")