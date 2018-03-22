class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ## find the median and calculate the sum of all distance between each element to the median
        nums = sorted(nums)
        return sum([nums[~i] - nums[i] for i in range(len(nums) / 2)])
        