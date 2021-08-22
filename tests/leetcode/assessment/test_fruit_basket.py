from unittest import TestCase
from leetcode.assessment.fruit_basket import FruitBasket


class TestFruitBasket(TestCase):

    def setUp(self):
        self.fruitBasket = FruitBasket()

    def test_store_fruit_in_basket(self):
        self.fail()

    def test_total_fruit_fixed_position(self):
        actual = self.fruitBasket.totalFruitFixedPosition([1, 2, 1])
        self.assertEqual(actual, 3)

    def test_total_fruit(self):
        actual = self.fruitBasket.totalFruit([0, 1, 2, 2])
        self.assertEqual(actual, 3)

    def test_total_fruit_two(self):
        actual = self.fruitBasket.totalFruit([1,2,3,2,2])
        self.assertEqual(actual, 4)


    def test_total_fruit_three(self):
        actual = self.fruitBasket.totalFruit([3,3,3,1,2,1,1,2,3,3,4])
        self.assertEqual(actual, 5)

    def test_total_fruit_four(self):
        actual = self.fruitBasket.totalFruit([0,0,1,1])
        self.assertEqual(4, actual)