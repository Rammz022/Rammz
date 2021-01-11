import random as rnd
from mashine.car import Car


class Passengers(Car):
    """Класс Пассажирская(Машина) P.s.в англ. языке  слово Пасажирская пишется как Passenger`s но называть класс так нельзя поэтому Passengers"""

    def __init__(self, car_name, class_name="Passengers Car", body="passengers", engine="gasoline",
                 shassis="front_wheel", transmission="manual", weight_over_3_tons=False):
        super().__init__(car_name, class_name)
        self.car_name = car_name
        self.class_name = class_name
        self.body = body
        self.engine = engine
        self.shassis = shassis
        self.transmission = transmission
        self.weight_over_3_tons = weight_over_3_tons
        """car_name - Название машины, class_name - класс машины(пассажирская,грузовая)"""

    def drive(self):
        self.min = 0
        if self.engine == "gasoline" and self.shassis == "front_wheel" and self.transmission == "manual":
            """Если машина классической сборки то шансы на поломку(не возможность ехать)меньше"""
            self.min -= 3
        self.max = 1
        if self.engine == "gasoline" and self.shassis == "front_wheel" and self.transmission == "manual":
            self.max += 2

        self.breaking = rnd.randint(self.min, self.max)
        if self.breaking >= 0:
            print("The car can be drive.")
        else:
            print("The car can`t be drive.")

    def can_transport_cargo(self):
        if not self.weight_over_3_tons:
            print("The car can`t transporting cargo.")
        else:
            print("The car can transporting cargo.")

    def can_transport_passengers(self):
        if not self.weight_over_3_tons:
            print("The car can transporting pessengers.")
        else:
            print("The car can`t transporting pessengers.")

    def change_assembly(self, engine, shassis, transmission):
        self.engine = engine
        self.shassis = shassis
        self.transmission = transmission

    def change_transporting_type(self, body):
        self.body = body

    def change_weight(self, weight_over_3_tons=bool):
        self.weight_over_3_tons = weight_over_3_tons

    def color(self, color):
        self.color = color
        print(self.color)
