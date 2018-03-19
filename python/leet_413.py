class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        mlen = len(A)
        if mlen < 3:
            return 0
        initSeq = []
        for i in range(1, mlen - 1):
            if A[i] - A[i - 1] == A[i + 1] - A[i]:
                initSeq.append((i - 1, i + 1))
        resSeq = list(initSeq)
        while len(initSeq) > 0:
            (currStart, currEnd) = initSeq.pop(0)
            if currEnd + 1 < mlen and A[currEnd + 1] + A[currEnd - 1] == 2 * A[currEnd]:
                initSeq.append((currStart, currEnd + 1))
                resSeq.append((currStart, currEnd + 1))
        return len(resSeq)
        
        