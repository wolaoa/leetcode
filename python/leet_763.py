#!/bin/bash
#*:- encoding:utf8 -:*
class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        maxLen = len(S)
        calcArr = [[maxLen, 0] for i in range(26)]
        for i in range(maxLen):
            currChar = ord(S[i]) - ord('a')
            if i > calcArr[currChar][1]:
                calcArr[currChar][1] = i
            if i < calcArr[currChar][0]:
                calcArr[currChar][0] = i
        calcArr.sort()
        currStart = currEnd = 0
        res = []
        for char in calcArr:
            if char[0] == maxLen:
                break
            if char[0] > currEnd:
                # 超出阈值了，出现了一个新的线段
                res.append(currEnd - currStart + 1)
                currStart = char[0]
                currEnd   = char[1]
                continue
            else:
                if char[1] > currEnd:
                    currEnd = char[1]
        res.append(currEnd - currStart + 1)
        return res