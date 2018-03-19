class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numLen = len(nums)
        if numLen <= 1:
            return numLen
        maxLen = [1 for i in range(numLen)]
        
        for i in range(1, numLen):
            for j in range(i):
                if nums[i] > nums[j]:
                    maxLen[i] = max(maxLen[i], maxLen[j] + 1)
        
        return max(maxLen)