class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        gaps = []
        res = 0
        maxLen = len(s)

        # find all vaild gaps
        for i in range(maxLen):
            if s[i] == '(':
                stack.append(i)
            else:
                if len(stack) > 0:
                    gaps.append([stack.pop(), i])
        gaps.sort()
        newLen = len(gaps)
        if newLen == 0:
            return 0

        # merge adjecent or sub gaps
        startPos = gaps[0][0]
        endPos   = gaps[0][1]
        res = endPos - startPos + 1

        for nextGap in range(1, newLen):
            if gaps[nextGap][0] > endPos + 1:
                startPos = gaps[nextGap][0]
                endPos   = gaps[nextGap][1]
            elif gaps[nextGap][1] >= endPos:
                endPos   = gaps[nextGap][1]
            currMax = endPos - startPos + 1
            if currMax > res:
                res = currMax
        return res
