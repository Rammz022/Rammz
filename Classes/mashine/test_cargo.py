import unittest
from mashine.Cargo import Cargo

class TestCar(unittest.TestCase):
    def test_chance_to_drive(self):
        Cargo.__init__(Cargo, "Gaz", "Cargo", "cargo", "gasoline", "four_wheel", "manual", True)
        Cargo.drive(Cargo)
        print(Cargo.first_name + " " + Cargo.last_name)
        print(Cargo.body)
        print(Cargo.engine)
        print(Cargo.shassis)
        print(Cargo.transmission)
        print(Cargo.min)
        print(Cargo.max)
        Cargo.__init__(Cargo, "Maz", "Cargo", "cargo", "diesel", "four_wheel", "auto", True)
        Cargo.drive(Cargo)
        print(Cargo.first_name + " " + Cargo.last_name)
        print(Cargo.body)
        print(Cargo.engine)
        print(Cargo.shassis)
        print(Cargo.transmission)
        print(Cargo.min)
        print(Cargo.max)

    def test_weight_over_3_tons(self):
        Cargo.__init__(Cargo, "Gaz", "Cargo", "cargo", "gasoline", "four_wheel", "manual", True)
        first = Cargo.weight_over_3_tons
        Cargo.weight_over_3_tons = False
        second = Cargo.weight_over_3_tons
        Cargo.can_transport_pessenger(Cargo)
        Cargo.can_transport_cargo(Cargo)
        self.assertEqual(first, second)

if __name__ == '__name__':
    unittest.main()