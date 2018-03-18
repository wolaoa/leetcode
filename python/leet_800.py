class Solution(object):
    def trans(self, color):
        newColor = [0 for i in range(6)]
        for i in range(6):
            if color[i] >= 'a':
                newColor[i] = ord(color[i]) - ord('a') + 10
            else:
                newColor[i] = ord(color[i]) - ord('0')
        digits = [0 for i in range(3)]
        res = '#'
        for i in range(3):
            digits[i] = (newColor[i * 2] * 16 + newColor[1 + i * 2])
            expected = 15
            for j in range(16):
                if digits[i] < self.dual[j]:
                    expected = j
                    break
            if self.dual[expected] - digits[i] >= digits[i] - self.dual[expected - 1]:
                expected -= 1
            if expected < 10:
                expected = chr(ord('0') + expected)
            else:
                expected = chr(ord('a') + expected - 10)
            res += expected + expected
        return res
    
    def similarRGB(self, color):
        """
        :type color: str
        :rtype: str
        """
        self.dual = [(i * 17) for i in range(16)]
        res = self.trans(color[1:])
        return res
        