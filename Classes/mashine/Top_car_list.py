from mashine.Car import Car

Car.top_transport(Car)

Car.show_word(Car)

print("Press 'q' for quit. \n")
while True:
    list = input("Car: ")
    if list == 'q':
        break
    Car.store_top_answer(Car, list)

print("\n Thanks for you top")
Car.show_top_answers(Car)
