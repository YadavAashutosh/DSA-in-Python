class Solution:
    def mySqrt(self, x: int) -> int:
        l=0
        r=x
        ans=0
        while l<=r:
            mid = (l+r)//2
            
            if mid**2>x:
                r=mid-1
            else:
                l=mid+1
                ans=mid
        return ans

obj = Solution()

print(obj.mySqrt(4))   # Output: 2
print(obj.mySqrt(8))   # Output: 2
print(obj.mySqrt(17))  # Output: 4
print(obj.mySqrt(0))   # Output: 0