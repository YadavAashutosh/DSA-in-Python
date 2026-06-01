# BEST CASE: O(N^2)
# WORST CASE: O(N^2)
# SPACE COMPLEXITY: O(1)

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        for i in range (len(nums)):
            mn = nums[i]
            ind=i
            for j in range(i+1,len(nums)):
                if nums[j]<mn:
                    mn = nums[j]
                    ind=j
            temp=nums[i]
            nums[i]=nums[ind]
            nums[ind]=temp
        return nums

        
    
o = Solution()
print(o.sortArray([5,1,1,2,0,0]))
print(o.sortArray([5,2,3,1]))
print(o.sortArray([-1,2,-3,4,0]))

# [0, 0, 1, 1, 2, 5]
# [1, 2, 3, 5]
# [-3, -1, 0, 2, 4]