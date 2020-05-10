"""
@project: Leet_Code

@author: gemoy

@file: The_nearest_common_ancestor_of_a_binary_tree.py

Create on 2020/5/10 21:17

Contact author by e-mail: gemo-yk@outlook.com
"""


class TreeNode(object):
    # Definition for a binary tree node.
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Tree(object):
    #create a tree
    def create_tree(self, nums_list):
        for num in nums_list:
            tree = TreeNode(num)
            tree.left = TreeNode()
            self.create_tree(tree.l_child)
            tree.r_child = TreeNode()
            self.create_tree(tree.r_child)


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return root
        if root.val == p.val or root.val == q.val:
            return root
        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)
        if l and r:
            return root
        if l:
            return l
        if r:
            return r


if __name__ == "__main__":
    solution = Solution()
    nums = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]


    # for idx, num in enumerate(nums):
    #     if idx < len(nums):
    #         node = TreeNode(num)


    root = TreeNode(nums[0])
    root.left = TreeNode(nums[1])
    root.right = TreeNode(nums[2])
    print()

