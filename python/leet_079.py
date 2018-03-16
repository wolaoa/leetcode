class Solution(object):
    def checkVaild(self, i, j, visited, index):
        if i < 0 or i >= self.m or j < 0 or j >= self.n or visited[i][j] == 1:
            return False
        if self.board[i][j] != self.word[index]:
            return False
        visited[i][j] = 1
        if index == len(self.word) - 1:
            return True
        ## check four directions
        res = self.checkVaild(i - 1, j, visited, index + 1) or self.checkVaild(i + 1, j, visited, index + 1) \
            or self.checkVaild(i, j - 1, visited, index + 1) or self.checkVaild(i, j + 1, visited, index + 1)
        if res == True:
            return True
        else:
            visited[i][j] = 0
            return False
    
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        self.board = board
        self.word  = word
        self.m = len(board)
        self.n = len(board[0])
        self.k = len(word)
        if self.m <= 0 or len(word) <= 0 or self.k > self.m * self.n:
            return False
        wordList = {}
        tarWordList = {}
        visited = [[0 for i in range(self.n)] for j in range(self.m)]
        for i in range(self.m):
            for j in range(self.n):
                if wordList.get(board[i][j], False) == False:
                    wordList[board[i][j]] = []
                wordList[board[i][j]].append(i * self.n + j)
        for ind in range(self.k):
            if tarWordList.get(word[ind], False) == False:
                tarWordList[word[ind]] = 1
            else:
                tarWordList[word[ind]] += 1
        
        if wordList.get(word[0], False) == False:
            return False
        for char, cnt in tarWordList.items():
            if wordList.get(char, False) == False or len(wordList[char]) < cnt:
                return False
        for pos in wordList[word[0]]:
            startI = pos / self.n
            startJ = pos % self.n
            if self.checkVaild(startI, startJ, visited, 0) == True:
                return True
        return False