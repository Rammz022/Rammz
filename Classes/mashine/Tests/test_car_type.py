import unittest
from mashine.Car_Type import Car_Type


class TestCar(unittest.TestCase):
    def setUp(self):
        self.my_answer = Car_Type("Test_Car")

    def test_weight_over_3_tons(self):
        Car_Type.__init__(self.my_answer, "Oda", "Pessengers", "pessengers", "gasoline", "front_wheel", "manual", True)
        first = self.my_answer.weight_over_3_tons
        print(self.my_answer.weight_over_3_tons)
        self.my_answer.weight_over_3_tons = False
        print(self.my_answer.weight_over_3_tons)
        second = self.my_answer.weight_over_3_tons
        self.my_answer.can_transport()
        self.assertEqual(first, second)

    def test_color(self):
        first = input("First Car Color: ")
        second = input("Inter Word to Compare: ")
        self.my_answer.change_color(first)
        self.assertEqual(first, second)


if __name__ == '__name__':
    unittest.main()
