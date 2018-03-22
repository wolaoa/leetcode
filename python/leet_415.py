class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        len1 = len(num1)
        len2 = len(num2)
        if len(num2) > len(num1):
            return self.addStrings(num2, num1)
       
	# malloc enough space to store res 
        res = [0 for i in range(len1 + 1)]
        i = len1 - 1
	# apply add operation
        for j in range(len2 - 1, -1, -1):
            res[i + 1] += int(num1[i]) + int(num2[j])
            res[i]     += res[i + 1] / 10
            res[i + 1] %= 10
            i -= 1
        # handle remain data
        for k in range(i, -1, -1):
            res[k + 1] += int(num1[k])
            res[k]     += res[k + 1] / 10
            res[k + 1] %= 10
        
	# convert int list to string
        resStr = '' . join([str(k) for k in res])
        
	# omit leading zeros
	start = 0
        while start < len(resStr) and resStr[start] == '0':
            start += 1
        
        if start == len(resStr):
            return '0'
        else:
            return resStr[start:]
            
        
