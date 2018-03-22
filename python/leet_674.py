class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxLen = 1
        numLen = len(nums)
        if numLen <= 1:
            return numLen
        currLen = 1
        for i in range(1, numLen):
            if nums[i] > nums[i - 1]:
                currLen += 1
            else:
                if currLen > maxLen:
                    maxLen = currLen
                currLen = 1
        if currLen > maxLen:
            maxLen = currLen
        return maxLen
        