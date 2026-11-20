class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        

        #iter- sell

        sol = 0

        for sell in range(1,len(prices)):
            buy = 0
            while buy<sell:
                profit = prices[sell]-prices[buy]
                if profit>sol:
                    sol=profit
                else: #sol>profit
                    buy+=1
            
        return sol


       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
        # b=0
        # s=1
        # profit = 0

        # while s<len(prices):
        #     if prices[b]<prices[s]:        
        #         tp = prices[s]-prices[b]
        #         profit = max(tp,profit)
        #     else:
        #         b=s
        #     s+=1
        # return profit