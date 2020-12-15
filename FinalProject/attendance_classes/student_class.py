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

        # error handling for inputs
        name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-")
        if not (name_characters.issuperset(lname) and name_characters.issuperset(fname)):
            raise ValueError
        if not isinstance(id, int):
            raise ValueError
        if not 900000000 <= id <= 900999999:
            raise ValueError
        self.last_name = lname
        self.first_name = fname
        self.id = id

    # display all parameters using str()
    def __str__(self):
        return str(self.id)+" "+ self.last_name + ", " + self.first_name

    # display all parameters using repr()
    def __repr__(self):
        return repr(self.id)+" "+ self.last_name + ", " + self.first_name


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pass
