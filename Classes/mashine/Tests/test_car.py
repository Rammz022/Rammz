import unittest
from mashine.Car import Car


class TestCar(unittest.TestCase):
    def setUp(self):
        self.my_answer = Car("Test_Car")
        self.answers = ['lada', 'nissan', 'chevrolet', 'bmw', 'audi']
        self.answersNegative = [[], True, 1]

    def test_store_single_answer(self):
        for answer in self.answers:
            self.my_answer.store_top_answer(answer)
            self.assertIn(answer, self.my_answer.answers)

    def test_store_negative_answer(self):
        for answer in self.answersNegative:
            self.my_answer.store_top_answer(answer)
            self.assertIn(answer, self.my_answer.answers)

    # def test_five_answers(self):
    #    for answer in self.answers:
    #        self.my_answer.store_top_answer(answer)
    #    for answer in self.answers:
    #        self.assertIn(answer, self.my_answer.store_top_answer(answer))

    # def test_error_writing(self):
    #    first = input("First Car: ")
    #    second = input("Second Car: ")
    #    self.assertEqual(first, second)


if __name__ == '__name__':
    unittest.main()
