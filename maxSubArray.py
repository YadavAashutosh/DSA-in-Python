class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currentsum=0
        maxsum=nums[0]
        for i in range(len(nums)):
            currentsum+=nums[i]
            if currentsum>maxsum:
                maxsum=currentsum
            if currentsum<0:
                currentsum=0
        return maxsum
    
ans=Solution()
print(ans.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(ans.maxSubArray([1]))
print(ans.maxSubArray([5,4,-1,7,8]))

# 6
# 1
# 23