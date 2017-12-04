class Solution(object):
    def bfs(self, matrix, i, j, last = 0):
        """
        :type matrix: List[List[int]]
        :type i: int current row index
        :type j: int current column index
        :rtype: void
        """
        if self.visited[i][j] == 0:
            self.visited[i][j] = 1
            self.res.append(matrix[i][j])
        retry = 0
        while retry < 4:
            if last % 4 == 0:
                if j + 1 <= self.n - 1 and self.visited[i][j + 1] == 0:
                    self.bfs(matrix, i, j + 1, last)
            elif last % 4 == 1: 
                if i + 1 <= self.m - 1 and self.visited[i + 1][j] == 0:
                    self.bfs(matrix, i + 1, j, last)
            elif last % 4 == 2:
                if j - 1 >= 0 and self.visited[i][j - 1] == 0:
                    self.bfs(matrix, i, j - 1, last)
            elif last % 4 == 3:
                if i - 1 >= 0 and self.visited[i - 1][j] == 0:
                    self.bfs(matrix, i - 1, j, last)
            last += 1
            retry += 1


    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        self.visited = []
        self.res = []
        self.m = len(matrix)
        if self.m == 0:
            # the matrix is empty
            return self.res
        self.n = len(matrix[0])
        for i in range(self.m):
            line = []
            for j in range(self.n):
                line.append(0)
            self.visited.append(line[:])
        self.bfs(matrix, 0, 0)
        return self.res
        
        