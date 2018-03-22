class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        ## 通俗来说， 保持一个皇位继承人序列，站在最前面的是皇帝， 后面一堆皇子。
        ## 其中，如果皇帝驾崩了， 就退出序列， 由太子继位
        ## 如果没有一把手没到时候，那么剩下的皇子谁的权重大，谁就把前面比他弱的都干掉
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
                
        