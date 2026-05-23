class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minp=prices[0]
        profit=0
        for i in range(len(prices)):
            currentprofit=prices[i]-minp
            if currentprofit>profit:
                profit = currentprofit
            minp = min(minp,prices[i])
        return profit 
           
ans=Solution()
print(ans.maxProfit([7,1,5,3,6,4]))#5