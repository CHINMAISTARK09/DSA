##Given an array prices[] of non-negative integers, representing the prices of the stocks on different days. The task is to find the maximum profit possible by buying and selling the stocks on different days when at most one transaction is allowed. Here one transaction means 1 buy + 1 Sell. If it is not possible to make a profit then return 0.

##Note: Stock must be bought before being sold.

    def maxProfit(self, prices):
        if len(prices)==1 or len(prices)==0:
            return 0
        else:
            min_amt=prices[0]
            profit=0
            for i in range(1,len(prices)):
                profit_curr=prices[i]-min_amt
                if profit_curr>profit:
                    profit=profit_curr
                if prices[i]<min_amt:
                    min_amt=prices[i]
            return profit 
            
