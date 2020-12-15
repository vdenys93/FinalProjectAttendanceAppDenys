""""
Author:Viktoria Denys
Program:attendance.py
Attendance class adding student info to a simple attendance list
"""
from datetime import date

from FinalProject.attendance_classes.student_class import Student


class Attendance:
    # Constructor to initialize the variables
    def __init__(self, attendance_id, student=(), attendance={}):
        """

        :int attendance_id:
        :Student student:
        :dict attendance:
        """
        # all  parameters
        self.attendance_id = attendance_id
        self.student = student
        self.attendance = attendance

    @property
    def attendance_id(self):
        return self._attendance_id

    @attendance_id.setter
    def attendance_id(self, value):
        # error handling
        if not isinstance(value, int):
            raise ValueError
        self._attendance_id = value

    @property
    def student(self):
        return self._student

    @student.setter
    def student(self, value):
        # error handling
        if not isinstance(value, Student):
            raise ValueError
        self._student = value

    def studentList(self, student):
        self.studentList.append(student)

    @property
    def attendance(self):
        return self._attendance

    @attendance.setter
    def attendance(self, value):
        # error handling
        if not isinstance(value, dict):
            raise ValueError
        self._attendance = value

    # Add an student to attendance  dictionary
    def add_item(self, dict):
        self.attendance.update(dict)

    # Create attendance list using dictionary
    def create_attendanceList(self):
        list = "Today`s attendance:\n"
        for key, value in self.attendance.items():
            list += "{} - {}\n".format(key, value)
        return print(list)
    # reset dictionary(removing info)
    def reset_attendanceList(self):
        self.attendanceList = {}

    # built-ins (str() and repr())
    def __str__(self):
        if self.attendance is None:
            return str(self.student) + "\nAttendance id =" + str(self.attendance_id)
        else:
            return str(self.student) + "\nAttendance id =" + str(self.attendance_id) + " attendance=" + str(
                self.attendance)

    def __repr__(self):
        if self.attendance is None:
            return repr(self.student) + "\nAttendance id =" + repr(self.attendance_id)
        else:
            return repr(self.student) + "\nAttendance id =" + repr(self.attendance_id) + ", attendance=" + repr(
                self.attendance)


# Driver code
tdate = date.today()
#creating objects
student = Student("Denys","Viktoriia")
student2 = Student("Gonzalez","Maria")
attendance = Attendance(1, student)
attendance2= Attendance(2,student2)

# adding student who presented in class to the dictionary
attendance.add_item({attendance.student.first_name+" "+attendance.student.last_name: tdate})
attendance2.add_item({attendance2.student.first_name+" "+attendance2.student.last_name: tdate})

# displaying attendance list
attendance.create_attendanceList()

# removing objects
del(attendance)
del(attendance2)
del(student)
del(student2)




