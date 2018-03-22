class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        aArr = a.split('+')
        bArr = b.split('+')
        aR = int(aArr[0])
        aS = 0 # sign
        if aArr[1][0] == '-':
            aS = 1
            aArr[1] = aArr[1][1:]
        #subfix
        aC = int(aArr[1][:-1])
        aC = -aC if aS == 1 else aC
        bR = int(bArr[0])
        bS = 0  #sign
        if bArr[1][0] == '-':
            bS = 1
            bArr[1] = bArr[1][1:]
        #subfix
        bC = int(bArr[1][:-1])
        bC = -bC if bS == 1 else bC
        
        #calc
        rPart = aR * bR - aC * bC
        cPart = aR * bC + bR * aC
        print rPart, cPart
        return "%d+%di" % (rPart, cPart)
