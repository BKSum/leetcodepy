from typing import List


class FruitBasket:

    def storeFruitInBasket(self, basketOne, basketTwo, fruit):
        if not basketOne:
            basketOne.append(fruit)
            return True
        elif fruit == basketOne[0]:
            basketOne.append(fruit)
            return True
        elif not basketTwo:
            basketTwo.append(fruit)
            return True
        elif fruit == basketTwo[0]:
            basketTwo.append(fruit)
            return True
        else:
            return False

    def totalFruitFixedPosition(self, fruits: List[int]) -> int:
        basketOne = []
        basketTwo = []
        for fruit in fruits:
            if not self.storeFruitInBasket(basketOne, basketTwo, fruit):
                break
        return len(basketOne) + len(basketTwo)

    def totalFruitx(self, fruits: List[int]) -> int:
        maxFruits = []
        distinctFruits = len(set(fruits))
        if distinctFruits<=2:
            return len(fruits)
        for counter in range(len(fruits)):
            maxFruits.append(self.totalFruitFixedPosition(fruits[counter:]))
        return max(maxFruits)

    def totalFruit(self, fruits: List[int]) -> int:
        storedMax = currentMax = count_b = a = b = 0
        for fruit in fruits:
            currentMax = currentMax + 1 if fruit in (a, b) else count_b + 1
            count_b = count_b + 1 if fruit == b else 1
            if b != fruit: a, b = b, fruit
            storedMax = max(storedMax, currentMax)
        return storedMax