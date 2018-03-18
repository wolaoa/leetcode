class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        mLen = len(cost)
        if mLen == 1:
            return cost[0]
        if mLen == 2:
            return min(cost[0], cost[1])
        
        for i in range(2, mLen):
            cost[i] += min(cost[i - 2], cost[i - 1])
        
        return min(cost[i], cost[i - 1])