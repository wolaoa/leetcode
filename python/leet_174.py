class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        m = len(dungeon)
        if m <= 0:
            return 1
        n = len(dungeon[0])
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i == m - 1 and j == n - 1:
                    cust = dungeon[i][j]
                elif i == m - 1: # last line
                    cust = dungeon[i][j] + dungeon[i][j + 1]
                elif j == n - 1:
                    cust = dungeon[i][j] + dungeon[i + 1][j]
                else:
                    cust = dungeon[i][j] + max(dungeon[i][j + 1], dungeon[i + 1][j])
                dungeon[i][j] = (cust if cust < 0 else 0)
        final = 1 - (dungeon[0][0] if dungeon[0][0] < 0  else 0)
        return final


