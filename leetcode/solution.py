# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    # For call to repr(). Prints object's information
    def __repr__(self):
        return 'TreeNode(%s, %s, %s)' % (self.val, self.left, self.right)

    # For call to repr(). Prints object's information
    def __str__(self):
        return 'TreeNode(%s)' % (self.val)

        # # For call to str(). Prints readable form
    # def __str__(self):
    #     return 'Value(%s), Left(%s), Right(%s)' % (self.val, self.left, self.right)

class Solution:

    def bfs(self, root, u):
        queue = [root]
        while queue:
            current = queue.pop(0)
            # print(current)
            if current.val == u:
                return queue.pop(0)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        return None

    def findNearestRightNode(self, root: TreeNode, u: TreeNode) -> TreeNode:
        x = self.bfs(root, u)
        print(x)
        #find if u exists
        #print right of u
        return x