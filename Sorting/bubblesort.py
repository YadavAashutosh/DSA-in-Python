# BEST CASE: O(N)
# WORST CASE: O(N^2)
# SPACE COMPLEXITY: O(1)

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            isSwap=False
            for j in range(len(nums)-i-1):
                if nums[j]>nums[j+1]:
                    temp = nums[j]
                    nums[j]=nums[j+1]
                    nums[j+1]=temp
                    isSwap = True
            if isSwap==False:
                break
        return nums
    
o = Solution()
print(o.sortArray([5,1,1,2,0,0]))
print(o.sortArray([5,2,3,1]))
print(o.sortArray([-1,2,-3,4,0]))

# [0, 0, 1, 1, 2, 5]
# [1, 2, 3, 5]
# [-3, -1, 0, 2, 4]