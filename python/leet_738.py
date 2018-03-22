class Solution(object):
    def monotoneIncreasingDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        strN = str(N)
        lenN = len(strN)
        if lenN <= 1:
            return N
        arrN = []
        for char in strN:
            arrN.append(int(char))

        currIndex = lenN
        for i in range(0, lenN - 1):
            if arrN[i] > arrN[i + 1]:
                currIndex = i
                break
        if currIndex == lenN:
            return N

        while currIndex >= 0:
            arrN[currIndex] -= 1
            if currIndex == 0 or arrN[currIndex] >= arrN[currIndex - 1]:
                frontStr =  '' . join(i.__str__() for i in arrN[:currIndex + 1])
                tailStr = '{0}' . format('9' * (lenN - currIndex - 1))
                strN = '' . join([frontStr, tailStr])
                break
            currIndex -= 1
        return int(strN)
        
        
                
