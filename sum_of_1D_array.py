class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        output = []
        for i in range (len(nums)):
            if i==0:
                output.append(nums[i])
            else:
                output.append(output[i-1]+nums[i])
        return output
a= Solution()
print(a.runningSum([1,2,3,4]))
print(a.runningSum([1,1,1,1,1]))
print(a.runningSum([3,1,2,10,1]))