class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
	strLen1 = len(num1)
	strLen2 = len(num2)
	resList = []
	# init the res list with zeros
	for k in range(strLen1 + strLen2):
	    resList.append(0)
        for i in range(strLen1 -1, -1, -1):
	    for j in range(strLen2 -1, -1, -1):
		int1 = int(num1[i])
		int2 = int(num2[j])
		resList[i + j + 1] += int1 * int2
		resList[i + j]     += resList[i + j + 1] / 10
	        resList[i + j + 1] %= 10
        resStrList = [str(i) for i in resList]	
	resStr = ''.join(resStrList)
	
	## omit leading zero
	start = 0
	while start < strLen1 + strLen2 and resStr[start] == '0':
	    start += 1
	
	if start == strLen1 + strLen2:
	    return '0'
	else:
	    return resStr[start:]
	
	
	
		
