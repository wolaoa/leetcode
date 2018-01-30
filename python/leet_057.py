#Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        res = []
        insertNew = False
        for interval in intervals:
            if interval.end < newInterval.start:
                res.append(interval)
            elif interval.start > newInterval.end:
                if insertNew == False:
                    res.append(newInterval)
                    insertNew = True
                res.append(interval)
            else:
                if interval.end >= newInterval.end:
                    newInterval.end = interval.end
                if interval.start <= newInterval.start:
                    newInterval.start = interval.start
        if insertNew == False:
            res.append(newInterval)        
        return res
        