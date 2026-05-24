class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        ans=0
        for i in accounts:
            ans = max(ans,sum(i))
        return ans
        
output= Solution()
print(output.maximumWealth([[1,5],[7,3],[3,5]])) #10