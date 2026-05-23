class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        for i in range(len(prices)-1):
            if prices[i+1]>prices[i]:
                profit+=prices[i+1]-prices[i]
        return profit
ans=Solution()
print(ans.maxProfit([7,1,5,3,6,4]))#7