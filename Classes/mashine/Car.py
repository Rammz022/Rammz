import random as rnd


class Car:
    def __init__(self, car_name, class_name="Car", color="Black"):
        self.word = ""
        self.car_name = car_name
        self.class_name = class_name
        self.color = color
        self.answers = []
        self.breaking = 1
        self.random = rnd.randint(0, 1)

    def drive(self):
        self.breaking = self.random
        if self.breaking == 0:
            print("The car can be drive.")
        else:
            print("The car can`t be drive.")

    def repair(self):
        repair = self.random
        if repair == 0:
            self.breaking = 0
            print("The car now repair and can drive.")
        else:
            self.breaking = 1
            print("The car now broken and can`t drive.")

    def can_transport_cargo(self):
        can_transport_cargo = self.random
        if can_transport_cargo == 0:
            print("The car can transporting cargo")
        else:
            print("The car can`t transporting cargo")

    def can_transport_passengers(self):
        can_transport_passengers = self.random
        if can_transport_passengers == 0:
            print("The car can transporting passengers.")
        else:
            print("The car can`t transporting passengers.")

    def top_transport(self, word="Write you own top of car"):
        if isinstance(word, str):
            self.word = word
        else:
            print("Word is not string type!")

    def show_word(self):
        print(self.word)

    def store_top_answer(self, new_answer):
        if isinstance(new_answer, str):
            self.answers.append(new_answer)
        else:
            print("New answer is not string type!")

    def show_top_answers(self):
        print("This is you top of car:")
        for answer in self.answers:
            print('- ' + answer)
