class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        import numpy as np
        if n <= 0:
            return False
        
        while n % 2 == 0:
            n /= 2
        
        if n > 1:
            return False
        else:
            return True
