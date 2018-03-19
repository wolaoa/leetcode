class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res = 0
        self.rows = len(grid)
        if self.rows == 0:
            return res
        self.columns = len(grid[0])
        for i in range(self.rows):
            for j in range(self.columns):
                if i == 0 and j == 0:
                    continue
                elif j == 0:
                    grid[i][j] += grid[i - 1][j]
                elif i == 0:
                    grid[i][j] += grid[i][j - 1]
                else:
                    grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
        return grid[self.rows  - 1][self.columns - 1] 