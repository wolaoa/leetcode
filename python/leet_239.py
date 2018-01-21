class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        maxSeq = []
        orderQueue = []
        
        for index, value in enumerate(nums):
            # if last maxvalue miss the window, omit it
            if orderQueue and orderQueue[0] <= index - k:
                orderQueue = orderQueue[1:]
            # popup the value which less then currentVal
            while orderQueue and nums[orderQueue[-1]] < value:
                orderQueue.pop()
            orderQueue.append(index)
            
            # when visited seq len meet k, append the maxVal to the anslist
            if index + 1 >= k:
                maxSeq.append(nums[orderQueue[0]])
            
        return maxSeq
                
        