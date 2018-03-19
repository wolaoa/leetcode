class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """

        # common iter  times[i] = min(times[i], times[i - j] + 1)
        times = [amount + 1 for i in range(amount + 1)]
        times[0] = 0
        for i in range(1, amount + 1):
            for j in coins:
                if j <= i:
                    times[i] = min(times[i], times[i - j] + 1)
        return times[amount] if times[amount] < amount + 1 else  -1
        


