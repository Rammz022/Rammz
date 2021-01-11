import unittest
from mashine.Passenger import Passengers

class TestCar(unittest.TestCase):
    def test_weight_over_3_tons(self):
        Passengers.__init__(Passengers, "Oda", "Pessengers", "pessengers", "gasoline", "front_wheel", "manual", True)
        first = Passengers.weight_over_3_tons
        print(Passengers.weight_over_3_tons)
        Passengers.weight_over_3_tons = False
        print(Passengers.weight_over_3_tons)
        second = Passengers.weight_over_3_tons
        Passengers.can_transport_pessengers(Passengers)
        Passengers.can_transport_cargo(Passengers)
        self.assertEqual(first, second)

    def test_color(self):
        first = input("First Car Color: ")
        second = input("Inter Word to Compare: ")
        Passengers.color(Passengers, first)
        self.assertEqual(first, second)

    #def test_weight(self):
        #first = input("Inter Word to Compare: ")
        #Passengers.change_weight(Passengers, first)
        #self.assertEqual(first, True)

if __name__ == '__name__':
    unittest.main()