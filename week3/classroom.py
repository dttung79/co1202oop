# from file_name import ClassName

from student import Student

class ClassRoom:
    def __init__(self, name):
        self.__name = name
        self.__students = []

    def get_name(self):
        return self.__name
    
    def set_name(self, new_name):
        if new_name != "":
            self.__name = new_name
        else:
            print("Classroom name cannot be empty")
    
    def add(self, new_student):
        self.__students.append(new_student)
        print(f'Student {new_student.get_name()} has been added.')
    
    def remove(self, student_id):
        for student in self.__students:
            if student.get_id() == student_id:
                self.__students.remove(student)
                print(f'Student {student.get_name()} has been removed.')
                return
        print(f'Student with ID {student_id} not found.')
    
    def show(self):
        print(f"Classroom: {self.__name}")
        print('-' * 20)
        for student in self.__students:
            student.show()
            print('-' * 20)
    
    def best_student(self):
        best_student = self.__students[0]
        for s in self.__students:
            if s.get_gpa() > best_student.get_gpa():
                best_student = s
        
        return best_student
    
    def avg_gpa(self):
        sum_gpa = 0
        for s in self.__students:
            sum_gpa += s.get_gpa()
        
        return sum_gpa / len(self.__students)