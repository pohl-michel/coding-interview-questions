from typing import Optional
#from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        else:
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
    
    def iterDFSMaxDepth(self, root: Optional[TreeNode]) -> int:
        pass

    def BFSMaxDepth(self, root: Optional[TreeNode]) -> int:
        pass


my_tree = TreeNode(val=3)
my_tree.left = TreeNode(val=9)
my_tree.right = TreeNode(val=20)
my_tree.right.left = TreeNode(val=15)
my_tree.right.right = TreeNode(val=7)

my_2nd_tree = TreeNode(val=1)
my_2nd_tree.right = TreeNode(val=2)

print(Solution().maxDepth(my_tree))
print(Solution().maxDepth(my_2nd_tree))


# Rk: solutions here: https://www.youtube.com/watch?v=hTM3phVI6YQ
# To do: code the solution with iterative depth-first search and breadth first search. 