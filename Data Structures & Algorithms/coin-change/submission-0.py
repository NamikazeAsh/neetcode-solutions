class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        d = {}
        def helper(amount):
            if amount == 0: return 0
            if amount in d: return d[amount]

            result = 1e9
            for coin in coins:
                if amount-coin>=0:
                    result = min(result,1+helper(amount-coin))

            d[amount] = result
            return result

    
        minCoins = helper(amount)

        if minCoins >= 1e9:
            return -1
        else:
            return minCoins
