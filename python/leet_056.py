#Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        setLen = len(intervals)
        if setLen <= 1:
            return intervals
        
        intervals = sorted(intervals, key=lambda x: x.start)
        
        currGap = intervals[0]
        res = []
        for i in range(1, setLen):
            if intervals[i].start > currGap.end:
                res.append(currGap)
                currGap = intervals[i]
            else:
                if intervals[i].end > currGap.end:
                    currGap.end = intervals[i].end
        res.append(currGap)
        return res
            
        