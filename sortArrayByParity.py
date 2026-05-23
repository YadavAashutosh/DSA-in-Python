class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        a=0
        for i in range(len(nums)):
            if nums[i]%2==0:
                temp=nums[a]
                nums[a] = nums[i]
                nums[i] = temp
                a+=1
        return nums

ans = Solution()
print(ans.sortArrayByParity([3,1,2,4]))
print(ans.sortArrayByParity([0]))

# [2, 4, 3, 1]
# [0]



