class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ans = []
        for i in candies:
            ans.append( i + extraCandies >= max(candies))
        return ans 
a= Solution()
print(a.kidsWithCandies([2,3,5,1,3],3))
print(a.kidsWithCandies([4,2,1,1,2],1))
print(a.kidsWithCandies([12,1,12],10))

# [True, True, True, False, True]
# [True, False, False, False, False]
# [True, False, True]