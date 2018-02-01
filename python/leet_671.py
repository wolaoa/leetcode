# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findAnother(self, root):
        # 当前val 不是最小值， 可能是第二小，无需再递归
        if root.val != self.black:
            return root.val

        # 当前val 与最小值相等，继续递归
        if root.left is None and root.right is None:
            return -1
        else:
            leftSecond = self.findAnother(root.left)
            rightSecond = self.findAnother(root.right)
            if leftSecond == -1:
                return rightSecond
            elif rightSecond == -1:
                return leftSecond
            else:
                return min(leftSecond, rightSecond)

    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.black = root.val
        return self.findAnother(root)
        