class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        total = 0
        serieLen = len(timeSeries)
        if serieLen == 0:
            return total
        if serieLen == 1:
            return duration
       
	# start point while be counted in 
        start = timeSeries[0]
        end   = start + duration - 1 
        
        for i in range(1, serieLen):
            if timeSeries[i] <= end:
                total += timeSeries[i] - start
            else:
                total += duration
            start = timeSeries[i]
            end = start + duration
        total += duration
        return total
