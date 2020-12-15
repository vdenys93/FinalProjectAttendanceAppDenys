""""
Author:Viktoria Denys
Program:student.py
Student class for general information of student
"""


# This is a base class.
# Press Double Shift to search everywhere for attendance_classes, files, tool windows, actions, and settings.


class Student:
    # unimplemented constructor
    def __init__(self, lname, fname, id=900000000):
        pass

    # display all parameters using str()
    def __str__(self):
        pass

    # display all parameters using repr()
    def __repr__(self):
        pass


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    student = Student()
    print(str(student))
