class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        listLen = len(timePoints)
        total = 24 * 60
        minites = [-1 for i in range(total)]
        for i in range(listLen):
            oneTime = timePoints[i].split(":")
            timeCount = int(oneTime[0]) * 60 + int(oneTime[1])
            if minites[timeCount] == timeCount:
                return 0
            minites[timeCount] = timeCount
        newList = [mini for mini in minites if mini != -1]
        newLen = len(newList)
        minimum = total
        for i in range(newLen - 1):
            A = newList[i] - newList[i + 1] if newList[i] - newList[i + 1] > 0 else newList[i + 1] - newList[i]
            B = total - A
            currentDiff = A if A <= B else B
            if currentDiff < minimum:
                minimum = currentDiff
        A = newList[newLen - 1] - newList[0] if newList[newLen - 1] - newList[0] > 0 else newList[0] - newList[newLen - 1]
        B = total - A
        currentDiff = A if A <= B else B
        if currentDiff < minimum:
            minimum = currentDiff
        
        return minimum
        
            
        