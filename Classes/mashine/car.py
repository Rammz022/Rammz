import random as rnd

class Car:
    def __init__(self, first_name, last_name="Car"):
        self.first_name = first_name
        self.last_name = last_name
        self.lists = []
    def drive(self):
        self.breaking = rnd.randint(0, 1)
        if self.breaking == 0:
            print("The car can be drive.")
        else:
            print("The car can`t be drive.")

    def can_transport_cargo(self):
        self.can_transport_cargo = rnd.randint(0, 1)
        if self.can_transport_cargo == 0:
            print("The car can transporting cargo")
        else:
            print("The car can`t transporting cargo")

    def can_transport_pessenger(self):
        self.can_transport_pessenger = rnd.randint(0, 1)
        if self.can_transport_pessenger == 0:
            print("The car can transporting pessengers")
        else:
            print("The car can`t transporting pessengers")

    def top_transport(self, word="Write you own top of car"):
        self.word = word
        self.lists = []

    def show_word(self):
        print(self.word)

    def store_top_list(self, new_list):
        self.lists.append(new_list)

    def show_top_list(self):
        print("This is you top of car:")
        for list in self.lists:
            print('- ' + list)