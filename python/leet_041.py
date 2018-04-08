class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mark = 1
        mLen = len(nums)
        count = 0
        minR  = 0
        for i in range(mLen):
            if nums[i] > 0:
                count += 1
                if minR == 0:
                    minR = nums[i]
                elif minR > nums[i]:
                    minR = nums[i]
        if count == 0 or minR != 1:
            return 1
        for i in range(mLen):
            if nums[i] > 0:
                mark |= 1 << min(nums[i], mLen + 1)
        res = 0
        while mark % 2 == 1:
            res += 1
            mark /= 2
        return res
        
