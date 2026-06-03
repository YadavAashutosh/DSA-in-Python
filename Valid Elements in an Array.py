from typing import List
class Solution:
    def findValidElements(self, nums: list[int]) -> list[int]:
        if len(nums)<3:
            return nums
        j=1
        while j<len(nums)-1:
            if max(nums[:j])<nums[j] or nums[j]>max(nums[(j+1):]):
                j+=1
            else:
                nums.pop(j)
        return nums
        

o = Solution()
print(o.findValidElements([1,2,4,2,3,2]))
print(o.findValidElements([5,5,5,5]))
print(o.findValidElements([1]))

# [1, 2, 4, 3, 2]
# [5, 5]
# [1]