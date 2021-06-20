from unittest import TestCase
from leetcode.solution import Solution, TreeNode


class TestSolution(TestCase):
    def test_findNearestRightNode(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)

        root.left.right = TreeNode(4)

        root.right.left = TreeNode(5)
        root.right.right = TreeNode(6)

        s = Solution()
        s.findNearestRightNode(root, 4)
