class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 1
        while n > 0:
            threshold = i * 9 * 10 ** (i - 1)
            if n <= threshold:
                m = (n % i if n % i > 0 else i)  # position
                k = 10 ** (i - 1) + (n - 1)/ i # num
                while i - m  > 0:
                    k /= 10
                    i -= 1
                return k % 10
            else:
                n -= threshold
            i += 1