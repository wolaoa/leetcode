class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 6:
            return False
        newSum = 1
        for x in range(2, 10001):
            if x ** 2 > num:
                break
            if num % x == 0:
                newSum += x + num / x
        if newSum == num:
            return True
        else:
            return False