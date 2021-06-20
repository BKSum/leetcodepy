import unittest
from leetcode.arrays.two_sum import SolutionTwo

class MyTestCase(unittest.TestCase):
    def test_something(self):
        actualList = SolutionTwo().twoSum([2, 7, 11, 15],9)
        self.assertListEqual([0, 1], actualList)

if __name__ == '__main__':
    unittest.main()
