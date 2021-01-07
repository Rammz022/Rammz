import unittest
from mashine.car import Car

class TestCar(unittest.TestCase):

    def test_store_single_list(self):
        word = "Write you own top of car"
        Car.top_transport(Car)
        Car.store_top_list(Car, "lada")

        self.assertIn("lada", Car.lists)

    def test_error_writing(self):
        first = input("First Car: ")
        second = input("Second Car: ")
        #Car.top_transport(Car)
        #Car.store_top_list(Car, first)
        #Car.store_top_list(Car, second)
        #for list in lists
            #list_member = list
        self.assertEqual(first, second)

if __name__ == '__name__':
    unittest.main()

