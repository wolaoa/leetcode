# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def middleSearch(self, root):
        if len(self.Klist) > self.k:
            return
        if root.left:
            self.middleSearch(root.left)
        self.Klist.append(root.val)
        if root.right:
            self.middleSearch(root.right)

    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.Klist = []
        self.k = k
        self.middleSearch(root)
        return self.Klist[k - 1]

        