class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        mlen = len(s)
        if mlen <= 1:
            return mlen
        # init
        currlist = []
        for i in range(mlen):
            currlist.append((i, i))
            if i >= 1 and s[i] == s[i - 1]:
                currlist.append((i - 1, i))
        res = list(currlist)
        # find
        while len(currlist) > 0:
            (start, end) = currlist.pop(0)
            # check Palindromic
            if start - 1 >= 0 and end + 1 < mlen and s[start - 1] == s[end + 1]:
                currlist.append((start - 1, end + 1))
                res.append((start - 1, end + 1))
        return len(res)
        
                    