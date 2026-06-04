class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l=0
        r=len(arr)-1
        while l<r:
            mid=(l+r)//2
            if arr[mid+1] > arr[mid]:
                l=mid+1
            else:
                r=mid
        return l

obj = Solution()

print(obj.peakIndexInMountainArray([0, 1, 0]))      # Output: 1
print(obj.peakIndexInMountainArray([0, 2, 1, 0]))   # Output: 1
print(obj.peakIndexInMountainArray([0, 10, 5, 2]))  # Output: 1