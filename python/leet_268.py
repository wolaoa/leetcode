class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxA = 0
        sumA = 0
        zeroShow = 0
        for num in nums:
            if num == 0:
                zeroShow = 1
                continue
            sumA += num
            if num > maxA:
                maxA = num
        
        miss = maxA * (maxA + 1) / 2 - sumA
        if miss == 0 and zeroShow > 0:
            miss = maxA + 1
        
        return miss