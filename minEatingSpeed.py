class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1
        r=max(piles)
        k=r
        while l<=r:
            mid =(l+r)//2
            totalhour = 0

            for pile in piles:
                totalhour+= (pile+mid-1)//mid
            if totalhour>h:
                l=mid+1
            else:
                k=mid
                r = mid-1
        return k
    
obj = Solution()

print(obj.minEatingSpeed([3, 6, 7, 11], 8))       # Output: 4
print(obj.minEatingSpeed([30, 11, 23, 4, 20], 5)) # Output: 30