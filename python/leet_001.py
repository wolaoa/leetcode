class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
	# STEP 1: sort the origin list 【O(nlogn)】
	sortedNum = sorted(nums)
        tempL = 0
        tempR = len(nums) - 1
	# STEP 2: find the two facto【O(n)】
        while tempL < tempR:
	    total = sortedNum[tempL] + sortedNum[tempR]  
            if total > target:
                tempR -= 1
            elif total < target:
                tempL += 1
            else:
                break
	if tempL == tempR:
	    return [-1, -1]
	# STEP 3: get index【O(n)】
	leftIndex  = nums.index(sortedNum[tempL])
	rightIndex = nums.index(sortedNum[tempR])
	if leftIndex == rightIndex:
	   rightIndex = nums[leftIndex + 1:].index(sortedNum[tempL]) + leftIndex + 1 
	return min(leftIndex, rightIndex),max(leftIndex, rightIndex)

