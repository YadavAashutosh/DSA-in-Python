# TC : O(n)

class Solution:
    def search(self, nums: List[int], target: int) -> int:

        for i in range(len(nums)):
            if nums[i]==target:
                return i 
        return -1
    
o = Solution()
print(o.search( [-1,0,3,5,9,12],9))#4
print(o.search( [-1,0,3,5,9,12],2))#-1