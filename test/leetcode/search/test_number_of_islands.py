import unittest
from leetcode.search.number_of_islands import Islands


class TestIslands(unittest.TestCase):
    def setUp(self):
        self.islands = Islands()

    def test_num_islands(self):
        self.islands.numIslands([[1,0],[0,1]])


if __name__ == '__main__':
    unittest.main()