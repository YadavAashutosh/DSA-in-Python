# TC : O(log(n))

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n= len(nums)
        l=0
        r=n-1
        while l<=r:
            mid=(l+r)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                r=mid-1
            else:
                l=mid+1
        return -1
     
o = Solution()
print(o.search( [-1,0,3,5,9,12],9))#4
print(o.search( [-1,0,3,5,9,12],2))#-1