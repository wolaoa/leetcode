class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        rows = len(matrix)
        if rows <= 0:
            return 0
        cols = len(matrix[0])
        res = []
        maxSqure = 0
        for i in range(rows):
            resRow = []
            for j in range(cols):
                if i == 0 or j == 0:
                    resRow.append(int(matrix[i][j]))
                    if maxSqure == 0 and matrix[i][j] == '1':
                        maxSqure = 1
                else:
                    resRow.append(0)
            res.append(resRow)

        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == '0':
                    continue
                else:
                    # compare adjacent three value, find the minimum one  
                    res[i][j] = min(res[i - 1][j], res[i][j -1], res[i - 1][j - 1]) + 1
                    if res[i][j] > maxSqure:
                        maxSqure = res[i][j]
        return maxSqure ** 2