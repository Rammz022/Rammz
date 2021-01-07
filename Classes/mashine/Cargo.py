import random as rnd
from mashine.car import Car


class Cargo(Car):
    def __init__(self, first_name, last_name="Cargo Car", body="cargo", engine="diesel", shassis="four_wheel",
                 transmission="auto", weight_over_3_tons=True):
        self.first_name = first_name
        self.last_name = last_name
        self.body = body
        self.engine = engine
        self.shassis = shassis
        self.transmission = transmission
        self.weight_over_3_tons = weight_over_3_tons

    def drive(self):
        self.min = 0
        if self.engine == "diesel" and self.shassis == "four_wheel" and self.transmission == "auto":
            self.min -= 3

        self.max = 1
        if self.engine == "diesel" and self.shassis == "four_wheel" and self.transmission == "auto":
            self.max += 2
        self.breaking = rnd.randint(self.min, self.max)
        if self.breaking >= 0:
            print("The car can be drive.")
        else:
            print("The car can`t be drive.")

    def can_transport_cargo(self):
        if self.weight_over_3_tons:
            print("The car can transporting cargo.")
        else:
            print("The car can`t transporting cargo.")

    def can_transport_passenger(self):
        if self.weight_over_3_tons:
            print("The car can`t transporting pessengers.")
        else:
            print("The car can transporting pessengers.")

    def color(self, color):
        self.color = color
        print(self.color)
