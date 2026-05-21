class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)<=2:
            return len(nums)
        
        a = 1
        for i in range(2,len(nums)):
            if nums[i]!=nums[a-1]:
                a+=1
                nums[a]=nums[i]
        return a+1
output = Solution()
print(output.removeDuplicates([1,1,1,2,2,3]))#Output: 5, nums = [1,1,2,2,3,_]
print(output.removeDuplicates([0,0,1,1,1,1,2,3,3]))#Output: 7, nums = [0,0,1,1,2,3,3,_,_]