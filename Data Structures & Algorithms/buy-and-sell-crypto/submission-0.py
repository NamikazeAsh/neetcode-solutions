class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b=0
        s=1
        profit = 0

        while s<len(prices):
            if prices[b]<prices[s]:        
                tp = prices[s]-prices[b]
                profit = max(tp,profit)
            else:
                b=s
            s+=1
        return profit