class Solution(object):
    def depthFirstSearch(self, candidates, target, index, ans):
        if target == 0:
            # fine a result, append to the final list
            if ans not in self.retList:
               self.retList.append(ans[:])
        # prevent out of list range
        maxLen = len(candidates)
        if index == maxLen:
            return
        for i in range(index, maxLen):
            if target < candidates[i]:
                # remain of the candidates all greater than target
                return
            ans.append(candidates[i])
            # each index can be used only once
            self.depthFirstSearch(candidates, target - candidates[i], i + 1, ans)
            ans.pop()
            
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int] may contain dumplicates
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
        
