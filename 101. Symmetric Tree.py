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
        # Создаем рекурсивную функцию проверки симметрии на каждом уровне
        def is_mirror(left, right):
            # если дерево закончилось
            if not left and not right:
                return True
            # если какие-то ветви дерева остались
            if not left or not right:
                return False
            # Возвращаем проверку значений текущего и следующего уровня слева и справа рекурсивно
            return (left.val == right.val) and is_mirror(left.left, right.right) and is_mirror(left.right, right.left)

        return is_mirror(root.left, root.right)


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(4)
root.right.right = TreeNode(3)

print(Solution().isSymmetric(root))

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)

print(Solution().isSymmetric(root))




