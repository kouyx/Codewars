"""
weekly-contest-94 (4)

leaf-similar-trees

考虑一个二叉树的所有叶子。这些叶子的值按从左到右的顺序排列形成一个 叶值序列 。

举个例子，给定一个如上图所示的树，其叶值序列为 (6, 7, 4, 9, 8) 。

如果两个二叉树的叶值序列相同，我们就认为它们是 叶相似的。

如果给定的两个头结点分别为 root1 和 root2 的树是叶相似的，返回 true；否则返回 false 。

提示：

给定的两个树会有 1 到 100 个结点。
TLE

test:
[3,5,1,6,2,9,8,null,null,7,4]
[3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        tree, leaf = [], []
        tree.append(root1)
        while tree:
            node = tree[-1]
            while node.left or node.right:
                tree.append(node)
                node = node.left if node.left else node.right
            leaf.append(tree.pop().val)
        leaf = leaf[::-1]
        tree.append(root2)
        while tree:
            node = tree[-1]
            while node.left or node.right:
                tree.append(node)
                node = node.left if node.left else node.right
            if leaf == [] or tree.pop().val != leaf.pop():
                return False
        return True
