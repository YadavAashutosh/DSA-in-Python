''' simple way but O(N)...

class Solution:
    def countOdds(self, low: int, high: int) -> int:
        count=0
        for i in range(low,high+1):
            if i%2==1:
                count+=1
        return count
'''
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return (high+1)//2 - low//2
odd = Solution()
odd.countOdds(3,10) # no output because return doesnt print 
print(odd.countOdds(3,10))