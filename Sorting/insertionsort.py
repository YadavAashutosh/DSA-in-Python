# BEST CASE: O(N)
# WORST CASE: O(N^2)
# SPACE COMPLEXITY: O(1)

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        for i in range (1,len(nums)):
            key= nums[i]
            j=i-1
            while j>=0 and nums[j]>key:
                nums[j+1] = nums[j]
                j-=1
            nums[j+1]=key
        return nums
    
o = Solution()
print(o.sortArray([5,1,1,2,0,0]))
print(o.sortArray([5,2,3,1]))
print(o.sortArray([-1,2,-3,4,0]))

# [0, 0, 1, 1, 2, 5]
# [1, 2, 3, 5]
# [-3, -1, 0, 2, 4]