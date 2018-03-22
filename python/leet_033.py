class Solution(object):
    def findTarget(self, nums, minIndex, maxIndex, target):
        """
        :type nums: List[index]
        :type minIndex: int 
        :type maxIndex: int
        :type target: int
        :rtype: int
        """
        if nums[minIndex] == target:
            return minIndex
        if nums[maxIndex] == target:
            return maxIndex

        if maxIndex == minIndex:
            return 0  if target == nums[minIndex] else -1

        median = (minIndex + maxIndex) / 2
        if nums[median] == target:
            return median

        if nums[median] > nums[minIndex] and nums[median] > nums[maxIndex]:
            # maxValue and minValue is in right part
            if target > nums[median] or target < nums[minIndex]:
                return self.findTarget(nums, median + 1, maxIndex, target)
            else:
                return self.findTarget(nums, minIndex, median, target)
        elif nums[median] < nums[minIndex] and nums[median] < nums[maxIndex]:
            # maxValue is in left part
            if target < nums[median] or target > nums[maxIndex]:
                return self.findTarget(nums, minIndex, median, target)
            else:
                return self.findTarget(nums, median + 1, maxIndex, target)
        else:
            # maxValue is in maxIndex and minValue is in minIndex
            if target < nums[minIndex] or target > nums[maxIndex]:
                return -1
            elif target > nums[median]:
                return self.findTarget(nums, median + 1, maxIndex, target)
            else:
                return self.findTarget(nums, minIndex, median, target)

        
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        numSize = len(nums)
        # the array is empty
        if numSize == 0:
            return -1
        minIndex = 0
        maxIndex = numSize - 1
        return self.findTarget(nums, minIndex, maxIndex, target)
