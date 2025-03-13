# learning setup in unittest

import unittest
from four_setup import Person

class TestPerson(unittest.TestCase):
    def setUp(self):
        self.p1 = Person('Hosein', 'Roosta')
        self.p2 = Person('Ali', 'Ahmadi')
        self.p3 = Person.fullname_two('Hosein', 'Roosta')
        self.p4 = Person.fullname_two('Ali', 'Ahmadi')
    def test_full_name(self):
        self.assertEqual(self.p1.full_name(), 'Hosein Roosta')
        self.assertEqual(self.p2.full_name(), 'Ali Ahmadi')
    def test_email(self):
        self.assertEqual(self.p1.email(), 'HoseinRoosta@gmail.com')
        self.assertEqual(self.p2.email(), 'AliAhmadi@gmail.com')
    def test_fullname_two(self):
        self.assertEqual(self.p3.full_name(),'Roosta Hosein')
        self.assertEqual(self.p4.full_name(),'Ahmadi Ali')

if __name__ == '__main__':
    unittest.main()