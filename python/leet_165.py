class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        ver1List = version1.split('.')
        ver2List = version2.split('.')
        verLen1 = len(ver1List)
        verLen2 = len(ver2List)
        if verLen1 == 0 or verLen2 == 0:
            return 0
        if verLen1 <= verLen2:
            for k in range(verLen1, verLen2):
                ver1List.append('0')
        else:
            for k in range(verLen2, verLen1):
                ver2List.append('0')
        maxLen = max(verLen1, verLen2)
        for i in range(maxLen):
            num1 = int(ver1List[i])
            num2 = int(ver2List[i])
            if num1 > num2:
                return 1
            elif num1 < num2:
                return -1
        return 0