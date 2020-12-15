import datetime
import unittest
from datetime import date

from FinalProject.attendance_classes import student_class as t
from FinalProject.attendance_classes import attendance_class as a


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.student = t.Student('Denys', 'Daisy')


    def tearDown(self):
        del self.student

    # testing constructor (valid info)
    def test_object_created_required_attributes(self):
        self.assertEqual(self.student.last_name, 'Denys')
        self.assertEqual(self.student.first_name, 'Daisy')

    # testing all valid parameters
    def test_object_created_all_attributes(self):
        student = t.Student('Denys', 'Daisy', 900000000)
        assert student.last_name == 'Denys'
        assert student.first_name == 'Daisy'
        assert student.id == 900000000

    # testing str method
    def test_student_str(self):
        student = t.Student('Denys', 'Daisy',900000000)
        self.assertEqual(str(student),"900000000 Denys, Daisy")

    # testing invalid last name
    def test_object_not_created_error_last_name(self):
        with self.assertRaises(ValueError):
            student = t.Student('123denys', 'Daisy', 900000000)
    # testing invalid first name
    def test_object_not_created_error_first_name(self):
        with self.assertRaises(ValueError):
            student = t.Student('Denys', '123daisy', 900000000)

    # testing invalid id (above required range)
    def test_object_not_created_error_id_high(self):
        with self.assertRaises(ValueError):
            student = t.Student('Denys', 'Daisy',1000000000)

    # testing invalid id (below required range)
    def test_object_not_created_error_id_low(self):
        with self.assertRaises(ValueError):
            student = t.Student('Denys', 'Daisy',899999999)

    #invalid format of id
    def test_object_not_created_error_id_bad(self):
        with self.assertRaises(ValueError):
            student = t.Student('Denys', 'Daisy',"none")

    # testing attendance
    def test_object_created_all_attendnce(self):
        student = t.Student('Denys', 'Daisy', 900000000)
        attendance = a.Attendance(1,student)
        assert student.last_name == 'Denys'
        assert student.first_name == 'Daisy'
        assert student.id == 900000000
        assert attendance.attendance_id == 1
        assert attendance.student == student





if __name__ == '__main__':
    unittest.main()
