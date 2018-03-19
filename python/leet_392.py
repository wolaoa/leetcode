class Solution(object):
    def binarySearch(self, seq, pos):
        # all pos less than pos, false
        mLen = len(seq)
        if seq[-1] < pos:
            return -1
        if seq[0] >= pos:
            return seq[0]
        if seq[-1] == pos:
            return pos
        mid = mLen / 2
        right = self.binarySearch(seq[:mid], pos)
        left = self.binarySearch(seq[mid:], pos)
        if right == left and right == -1:
            return -1
        elif right == -1:
            return left
        else:
            return right

    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        tLen = len(t)
        sLen = len(s)

        chrDict = {}
        for i in range(tLen):
            if chrDict.get(t[i], 0) == 0:
                chrDict[t[i]] = []
            chrDict[t[i]].append(i)

        pos = 0
        for j in range(sLen):
            ## char not exist on t, False
            if chrDict.get(s[j], 0) == 0:
                return False
            pos = self.binarySearch(chrDict[s[j]], pos)
            # no available candidate char
            if pos == -1:
                return False
            # find next char, start pos plus
            pos += 1
        return True

            

