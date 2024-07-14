"""
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
-------------
Дан корень бинарного дерева, проверьте является ли он отражением себя (например, симметрия вокруг центра).
-------------
Constraints:

    The number of nodes in the tree is in the range [1, 1000].
    -100 <= Node.val <= 100
-------------
EASY
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        pass



