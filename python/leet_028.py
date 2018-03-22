class Solution(object):
    def getNext(self, needle):
	"""
	:type needle: str
	:rtype list
	"""
	lenN = len(needle)
	nextList = [-1 for i in range(lenN)]
	j = -1
	i = 0
	while i < lenN - 1:
	    if j == -1 or needle[i] == needle[j]:
		i += 1
		j += 1
		if needle[i] != needle[j]:
		    nextList[i] = j
		else:
		    nextList[i] = nextList[j]
	    else:
		j = nextList[j]
	return nextList
	    
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
	lenN = len(needle)
	lenH = len(haystack)
	if lenN > lenH:
	    return -1
	indexH = indexN = 0
	nextList = self.getNext(needle)
	while indexN < lenN and indexH < lenH:
	    if indexN == -1 or haystack[indexH] == needle[indexN]:
		indexN += 1
		indexH += 1
	    else:
		indexN = nextList[indexN]
	# matched
	if indexN == lenN:
	    return indexH - lenN
	return -1

	     
