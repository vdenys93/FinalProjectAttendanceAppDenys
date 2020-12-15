"""
Author:Viktoria Denys
Program:dbms_GUI.py
GUI to add  student and view attendance list
"""

import tkinter
import tkinter.messagebox
from datetime import date
from tkinter import *
from FinalProject.dbms import student_dbms as db


class dbmsGUI:

    def __init__(self, window):
        # Connect to a SQLite database
        self.conn = db.create_connection("attendanceDBMS.db")
        window.title("Attendance tracker")
        window.geometry("500x500")
        # Button "Create Database & Table"
        self.b_create_table = tkinter.Button(window, height=1, width=20, text="Create Database & Table",
                                             command=lambda: self.create_db_table())
        self.b_create_table.pack()
        # Button "Add Student"
        self.e_lname = tkinter.Entry(window)
        self.e_fname = tkinter.Entry(window)
        self.e_lname.pack()
        self.e_fname.pack()
        self.b_add_student = tkinter.Button(window, height=1, width=20, text="Add Student",
                                           command=lambda: self.add_student())
        self.b_add_student.pack()

        # Button "Check In"
        self.l_pid = tkinter.Label(window, text="")
        self.e_date = date.today()
        self.l_table_data = tkinter.Label(window, text="")
        self.l_pid.pack()
        self.b_add_attendance = tkinter.Button(window, height=1, width=20, text="Check In",
                                            command=lambda: self.add_attendance())
        self.b_add_attendance.pack()


        # Button: "View Student Table"
        self.b_view_student = tkinter.Button(window, height=1, width=20, text="View Students",
                                            command=lambda: self.view_students())
        self.b_view_student.pack()
        # Button: "View Attendance Table for current date"
        self.b_view_attendance = tkinter.Button(window, height=1, width=20, text="Today`s attendance",
                                             command=lambda: self.view_attendance())
        self.b_view_attendance.pack()
        # Display rows in the GUI
        self.l_table_data = tkinter.Label(window, text="")
        self.l_table_data.pack()
        # Exit Button
        self.b_exit = tkinter.Button(app_window, height=1, width=20, text="Exit",
                                     command=lambda: app_window.destroy())
        self.b_exit.pack()

    def create_db_table(self):
        # call create_tables ()
        db.create_tables(self.conn)
        self.b_create_table.configure(state=tkinter.DISABLED)

    def add_student(self):
        # call create_student function
        student = (self.e_fname.get(), self.e_lname.get())
        student_id = db.create_student(self.conn, student)
        self.conn.commit()
        self.l_pid.configure(text=student_id)
        self.b_add_student.configure(state=tkinter.DISABLED)
        self.b_add_attendance.configure(state=tkinter.NORMAL)
        self.e_fname.delete(0, tkinter.END)
        self.e_lname.delete(0, tkinter.END)

    def add_attendance(self):
        # call create_attendance function
        attendance = (self.l_pid.cget("text"), self.e_date)
        attendance_id = db.create_attendance(self.conn, attendance)
        self.conn.commit()
        self.l_pid.configure(text=attendance_id)
        self.b_add_attendance.configure(state=tkinter.DISABLED)
        self.b_add_student.configure(state=tkinter.NORMAL)


    def view_students(self):
        # Query for all rows of Student
        rows = db.select_all_students(self.conn)
        text = ""
        for row in rows:
            for col in row:
                text += "{}      ".format(col)
            text += "\n"
        self.l_table_data.configure(text=text)

    def view_attendance(self):
        # Query for all rows of Attendance
        rows = db.select_all_attendance(self.conn)
        text = ""
        for row in rows:
            for col in row:
                text += "{}      ".format(col)
            text += "\n"
        self.l_table_data.configure(text=text)


app_window = tkinter.Tk()
dbms_app = dbmsGUI(app_window)
app_window.mainloop()

