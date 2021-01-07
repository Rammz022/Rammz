import unittest
from mashine.Passenger import Passenger

class TestCar(unittest.TestCase):
    def test_weight_over_3_tons(self):
        Passenger.__init__(Passenger, "Oda", "Pessenger", "pessenger", "gasoline", "front_wheel", "manual", True)
        first = Passenger.weight_over_3_tons
        print(Passenger.weight_over_3_tons)
        Passenger.weight_over_3_tons = False
        print(Passenger.weight_over_3_tons)
        second = Passenger.weight_over_3_tons
        Passenger.can_transport_pessenger(Passenger)
        Passenger.can_transport_cargo(Passenger)
        self.assertEqual(first, second)

    def test_color(self):
        first = input("First Car Color: ")
        second = input("Inter Word to Compare: ")
        Passenger.color(Passenger, first)
        self.assertNotEqual(first, int)
        self.assertNotEqual(first, None)
        self.assertNotEqual(first, float)
        self.assertNotEqual(first, list)
        self.assertEqual(first, second)

if __name__ == '__name__':
    unittest.main()