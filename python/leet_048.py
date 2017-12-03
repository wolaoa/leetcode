class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix) - 1
        middle = n / 2 + 1
        # 注意区分奇数阶 和偶数阶的区别
        if n % 2 == 0:
            # 奇数阶，防止对称轴重复翻转
            for i in range(middle):
                for j in range(middle - 1):
                    temp = matrix[i][j]
                    matrix[i][j] = matrix[n - j][i]
                    matrix[n - j][i] = matrix[n - i][n - j]
                    matrix[n - i][n - j] = matrix[j][n - i]
                    matrix[j][n - i] = temp
        else:
            for i in range(middle):
                for j in range(middle):
                    temp = matrix[i][j]
                    matrix[i][j] = matrix[n - j][i]
                    matrix[n - j][i] = matrix[n - i][n - j]
                    matrix[n - i][n - j] = matrix[j][n - i]
                    matrix[j][n - i] = temp