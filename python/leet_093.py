class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        sLen = len(s)
        res = []
        if sLen < 4 or sLen > 12:
            return res
        
        for i in range(1, sLen - 2):
            first = int(s[:i])
            if first > 255:
                break
            for j in range(i + 1, sLen - 1):
                second = int(s[i:j])
                if second > 255:
                    break
                for k in range(j + 1, sLen):
                    third = int(s[j:k])
                    if third > 255:
                        break
                    last = int(s[k:])
                    if last > 255:
                        continue
                    findOne = '.'.join([str(first), str(second), str(third), str(last)])
                    if len(findOne) == sLen + 3:
                        res.append(findOne)
        return res