from classroom import ClassRoom
from student import Student

class ClassRoomManagement:
    def __init__(self):
        name = input('Enter classroom name: ')
        self.__room = ClassRoom(name)
    
    def print_menu(self):
        print("CLASSROOM MANAGEMENT SYSTEM")
        print("1. Add student")
        print("2. Remove student")
        print("3. Show all students")
        print("4. Show best student")
        print("5. Quit")
    
    def add_student(self):
        # ask user to enter id, name and gpa
        id = int(input('Enter student ID: '))
        name = input('Enter student name: ')
        gpa = float(input('Enter student GPA: '))
        # create a new student object
        s = Student(id, name, gpa)
        # add the student to the classroom
        self.__room.add(s)
    
    def remove_student(self):
        id = int(input('Enter student ID to remove: '))
        self.__room.remove(id)
    
    def show_all_students(self):
        self.__room.show()
    
    def show_best_student(self):
        best = self.__room.best_student()
        print('Best student: ')
        best.show()

    def run(self):
        while True:
            self.print_menu()
            choice = int(input('Enter your choice: '))
            if choice == 1:
                self.add_student()
            elif choice == 2:
                self.remove_student()
            elif choice == 3:
                self.show_all_students()
            elif choice == 4:
                self.show_best_student()
            elif choice == 5:
                print('Goodbye!')
                break
            else:
                print('Invalid choice!')


####
if __name__ == "__main__":
    c = ClassRoomManagement()
    c.run()