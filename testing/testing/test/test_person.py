import unittest
import datetime
from testing.src.model.person import Person

class TestPerson(unittest.TestCase):

    def setUp(self):
        self.person = Person(
                            "Mr",
                            "Jane",
                            "Smith",
                            datetime.date(1992, 3, 12), # year, month, day
                            "No. 12 Short Street, Greenville",
                            "555 456 0987",
                            "jane.doe@example.com"
                        )

    def test_init(self):
        self.assertEqual(self.person.name, "Jane")
        self.assertEqual(self.person.surname, "Smith")

    def test_fullname(self):
        self.assertEqual(self.person.fullname, "Jane Smith")