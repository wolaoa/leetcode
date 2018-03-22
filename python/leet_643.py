class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        numLen = len(nums)
        if numLen <= k:
            return sum(nums) * 1.00 / k
        maxCnt = currCnt = sum(nums[:k])
        for i in range(k, numLen):
            currCnt  = currCnt + nums[i] - nums[i - k]
            if currCnt > maxCnt:
                maxCnt = currCnt
        return maxCnt * 1.00 / k
        