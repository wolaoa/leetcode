class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        currlist = []
        mLen = len(s)
        if mLen <= 1:
            return s

        res = 1
        start = 1
        end = 1
        for i in range(mLen):
            currlist.append((i, i))
            if i > 0 and s[i] == s[i - 1]:
                currlist.append((i - 1, i))
                start = i - 1
                end   = i
                res = 2
        
        while len(currlist) > 0:
            currStart, currEnd = currlist.pop(0)
            if currStart - 1 >= 0 and currEnd + 1 < mLen and s[currStart - 1] == s[currEnd + 1]:
                currlist.append((currStart - 1, currEnd + 1))
                if currEnd - currStart + 3 > res:
                    res = currEnd - currStart + 3
                    start = currStart - 1
                    end = currEnd + 1
        return s[start: end + 1]
            
        
        