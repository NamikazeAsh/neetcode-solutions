class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # d = {}
        # def helper(amount):
        #     if amount == 0: return 0
        #     if amount in d: return d[amount]

        #     result = 1e9
        #     for coin in coins:
        #         if amount-coin>=0:
        #             result = min(result,1+helper(amount-coin))

        #     d[amount] = result
        #     return result

    
        # minCoins = helper(amount)

        # if minCoins >= 1e9:
        #     return -1
        # else:
        #     return minCoins

        memo = {}

        for ai in range(amount+1):
            if ai==0:
                memo[ai]=0
            else:
                memo[ai]=float('inf')
                for coin in coins:
                    subproblem = ai - coin
                    if subproblem<0:
                        continue
                    memo[ai] = min(memo[ai],memo[subproblem]+1)
        res = memo[amount]
        return -1 if res==float('inf') else res