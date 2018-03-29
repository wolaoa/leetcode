class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        mlen = len(matrix)
        if mlen <= 0:
            return 
        nlen = len(matrix[0])
        slots = 0
        for i in range(mlen):
            for j in range(nlen):
                if matrix[i][j] == 0:
                    slots = slots | 1 << i | 1 << (mlen + j)
        for m in range(mlen):
            if (slots >> m) % 2 == 1:
                matrix[m][:] = [0 for i in range(nlen)]
                continue
            for n in range(nlen):
                if (slots >> (mlen + n)) % 2 == 1:
                    matrix[m][n] = 0