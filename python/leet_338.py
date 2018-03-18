class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        res = [0 for i in range(num + 1)]
        for i in range(num + 1):
            res[i] = res[i / 2] if i % 2 == 0 else res[i / 2] + 1
        return res
        