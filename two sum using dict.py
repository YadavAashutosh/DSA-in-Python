class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1 ={}
        for i in range(len(nums)):
            rem = target - nums[i]
            if rem in dict1:
                return [dict1[rem],i]
            dict1[nums[i]]=i
            
lists = Solution()
print(lists.twoSum([2,7,11,15],9))
print(lists.twoSum([3,2,4],6))
print(lists.twoSum([3,3],6))