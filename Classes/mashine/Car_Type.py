import random as rnd
from mashine.Car import Car


class Car_Type(Car):
    """Класс Пассажирская(Машина) P.s.в англ. языке  слово Пасажирская пишется как Passenger`s но называть класс так нельзя поэтому Passengers"""

    def __init__(self, car_name, class_name="Passengers", body="passengers", engine="gasoline",
                 shassis="front_wheel", transmission="manual", weight_over_3_tons=False, color="Blue"):
        super().__init__(car_name, class_name, color)
        self.body = body
        self.engine = engine
        self.shassis = shassis
        self.transmission = transmission
        self.weight_over_3_tons = weight_over_3_tons
        """car_name - Название машины, class_name - класс машины(пассажирская,грузовая)"""

    def drive(self):
        minimum = 0
        maximum = 1
        if self.engine == "gasoline" and self.shassis == "front_wheel" and self.transmission == "manual":
            """Если машина классической сборки то шансы на поломку(не возможность ехать)меньше"""
            minimum -= 3
            maximum += 2
        else:
            minimum -= 4
            maximum += 1
        self.breaking = rnd.randint(minimum, maximum)
        if self.breaking >= 0:
            print("The car can`t be drive.")
        else:
            print("The car can be drive.")

    def repair(self):
        if self.breaking >= 0:
            minimum = 0
            maximum = 1
            if self.transmission == "manual" and self.engine == "gasoline":
                minimum -= 1
                maximum += 2
            else:
                minimum -= 3
                maximum -= 1
            repair = rnd.randint(minimum, maximum)
            if repair >= 0:
                print("The car now repair and can drive.")
            else:
                print("The car now broken and can`t drive.")
                self.repair()
        else:
            print("The car already can drive.")

    def can_transport(self):
        if not self.weight_over_3_tons:
            print("The car can transporting passengers but can`t transporting cargo.")
        else:
            print("The car can`t transporting passengers but can transporting cargo.")

    def change_assembly(self, engine, shassis, transmission):
        self.engine = engine
        self.shassis = shassis
        self.transmission = transmission

    def change_class_type(self, body):
        self.body = body
        self.class_name = body

    def change_weight(self, weight_over_3_tons=bool):
        self.weight_over_3_tons = weight_over_3_tons

    def change_color(self, color):
        self.color = color
        print(self.color)
