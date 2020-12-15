"""
Author:Viktoria Denys
Program:dbms_connector.py

"""
import sqlite3
from datetime import date
from sqlite3 import Error


def create_connection(db):
    """ Connect to a SQLite database
    :param db: filename of database
    :return connection if no error, otherwise None"""
    try:
        conn = sqlite3.connect(db)
        return conn
    except Error as err:
        print(err)
    return None


def create_table(conn, sql_create_table):
    """ Creates table with give sql statement
    :param conn: Connection object
    :param sql_create_table: a SQL CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(sql_create_table)
    except Error as e:
        print(e)


def create_tables(conn):
    sql_create_student_table = """ CREATE TABLE IF NOT EXISTS student (
                                        id integer PRIMARY KEY,
                                        firstname text NOT NULL,
                                        lastname text NOT NULL
                                    ); """

    sql_create_attendance_table = """CREATE TABLE IF NOT EXISTS attendance (
                                    id integer PRIMARY KEY,
                                    today_date text NOT NULL,
                                    FOREIGN KEY (id) REFERENCES student (id)
                                );"""

    # create a database connection
    if conn is not None:
        # create projects table
        create_table(conn, sql_create_student_table)
        # create tasks table
        create_table(conn, sql_create_attendance_table)


    else:
        print("Unable to connect")


def create_student(conn, student):
    """Create a new person for table
    :param conn:
    :param student:
    :return: student id
    """
    sql = ''' INSERT INTO student(firstname,lastname)
              VALUES(?,?) '''
    cur = conn.cursor()  # cursor object
    cur.execute(sql, student)
    return cur.lastrowid  # returns the row id of the cursor object, the student id


def create_attendance(conn, attendance):
    """Create a new person for table
    :param conn:
    :param attendance:
    :return: attendance id
    """
    sql = ''' INSERT INTO attendance(id, today_date)
              VALUES(?,?) '''
    cur = conn.cursor()  # cursor object
    cur.execute(sql, attendance)
    return cur.lastrowid  # returns the row id of the cursor object, the attendance id


def select_all_students(conn):
    """Query all rows of student table
    :param conn: the connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM student")

    rows = cur.fetchall()

    return rows  # return the rows


def select_all_attendance(conn):
    """Query all rows of attendance table for current date
    :param conn: the connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT student.id,firstname, lastname, today_date  "
                "FROM attendance INNER JOIN student on student.id = attendance.id "
                "WHERE today_date = DATE('now', 'localtime')")

    rows = cur.fetchall()

    return rows  # return the rows


if __name__ == '__main__':

    conn = create_connection("pythonsqlite.db")
    create_tables(conn)

    with conn:
        # add a row into each of the tables:
        student = ('Rob', 'Thomas')
        student_id = create_student(conn, student)

        attendance = (student_id,date.today())
        attendance_id = create_attendance(conn, attendance)

    with conn:
        # return all student and attendance rows
        rows = select_all_students(conn)
        for row in rows:
            print(row)
        rows = select_all_attendance(conn)
        for row in rows:
            print(row)
