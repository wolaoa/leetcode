class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        cntArr = [0 for i in range(amount + 1)]
        cntArr[0] = 1
        # be careful of the order
        for coin in coins:
            for j in range(coin, amount + 1):
                cntArr[j] += cntArr[j - coin]
        return cntArr[amount]
