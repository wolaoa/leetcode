class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mLen = len(nums)
        if mLen <= 0:
            return 0
        elif mLen <= 2:
            return max(nums)
        nums[2] += nums[0]
        for i in range(3, mLen):
            nums[i] += max(nums[i - 2], nums[i - 3])
        
        return max(nums[-1], nums[-2])
        