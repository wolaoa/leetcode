#!/usr/bin/python
# -*- coding: UTF-8 -*-
class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 分解质因数的做法: 10 = 2 * 5
        # 10! 尾部0 的个数取决于 =>  2 ^(m) * 5 ^ (n)  
        # 且其中必有 m > n
        # 因此只需要关注可能出现的5的幂
        # f(n) = f(n / 5) + f(n / 5**2 ) + .... f(n / 5**k)  5 ** k < n < 5 **(k+1)
        ret = 0
        while n > 0:
            cnt = n / 5
            if cnt > 0:
                ret += cnt
            n = cnt
        return ret