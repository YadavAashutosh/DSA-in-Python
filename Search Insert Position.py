class Solution:
    def lowerbound(self,nums,target):
        ans=len(nums)
        l=0
        r=len(nums)-1
        while l<=r:
            mid = (l+r)//2
            if nums[mid]<target:
                l=mid+1
                
            elif nums[mid]==target:
                return mid
            elif nums[mid]>target:
                r=mid-1
                ans=mid
                
        return ans

    def searchInsert(self, nums: List[int], target: int) -> int:
        return self.lowerbound(nums,target)
obj = Solution()

print(obj.searchInsert([1, 3, 5, 6], 5))  # Output: 2
print(obj.searchInsert([1, 3, 5, 6], 2))  # Output: 1
print(obj.searchInsert([1, 3, 5, 6], 7))  # Output: 4