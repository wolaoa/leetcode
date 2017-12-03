class Solution(object):
    def depthFirstSearch(self, candidates, target, index, ans):
        if target == 0:
            # fine a result, append to the final list
            self.retList.append(ans[:])
        for i in range(index, len(candidates)):
            if target < candidates[i]:
                # remain of the candidates all greater than target
                return
            ans.append(candidates[i])
            self.depthFirstSearch(candidates, target - candidates[i], i, ans)
            ans.pop()
            
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # list of all possible combination results
        self.retList = []
        #  temp list obtain temp item from a dfs route
        ans = []
        #  first sort the candidates list
        #  to ensure the dfs get terminate condition
        candidates = sorted(candidates)
        self.depthFirstSearch(candidates, target, 0, ans)
        return self.retList
        