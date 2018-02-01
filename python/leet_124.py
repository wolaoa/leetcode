# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# [ Test case]
# [1,null,-7,-9,-8,null,null,3,null,null,-2]
# [-1, -2]
# [-2 , -1]
# [1, 2, 3]
# [-1, 1, 2, 3 ,5, 3]
# [-1]
# [0]
# [0, 1, 2, 5, 4, 5, -1]
# [-1, 10, 3, 2, 3, 100]
# [-3,-4,0,null,null,0,1,null,7,null,-3]
# [5,-5,-9,6,3,2,null,null,5,4,null,null,null,null,null,null,1]


class Solution(object):
    def findMaxPath(self, root):
        if root.left is None and root.right is None:
            if root.val > self.maxVal:
                self.maxVal = root.val
            return root.val
        
        leftVal = rightVal = None
        if root.left is None:
            rightVal = self.findMaxPath(root.right)
            currTreeMax = currPathMax = max(rightVal + root.val, root.val)
        elif root.right is None:
            leftVal = self.findMaxPath(root.left)
            currTreeMax = currPathMax = max(leftVal + root.val, root.val)
        else:
            leftVal = self.findMaxPath(root.left)
            rightVal = self.findMaxPath(root.right)
            subMax = max(leftVal, rightVal)
            if subMax > self.maxVal:
                self.maxVal = subMax
            currPathMax = max(subMax + root.val, root.val)
            currTreeMax = max(currPathMax, root.val + rightVal + leftVal)
        if currTreeMax > self.maxVal:
            self.maxVal = currTreeMax
        return currPathMax
        
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        self.maxVal = root.val
        if root.left is None and root.right is None:
            return self.maxVal
        elif root.left is None:
            rightVal = self.findMaxPath(root.right)
            return max(self.maxVal, root.val, rightVal, root.val + rightVal)
        if root.right is None:
            leftVal = self.findMaxPath(root.left)
            return max(self.maxVal, root.val, leftVal, root.val + leftVal)
        else:
            rightVal = self.findMaxPath(root.right)
            leftVal = self.findMaxPath(root.left)
            currMax = max(self.maxVal, root.val, root.val + leftVal + rightVal, root.val + leftVal, root.val + rightVal)
            return currMax