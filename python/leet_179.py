class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        numStrList = [str(item) for item in nums]
        numStrList.sort(lambda x, y: x + y if x + y > y + x else y + x)
        return '' .join(numStrList)
