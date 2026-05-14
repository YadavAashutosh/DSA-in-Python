class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans=[]
        for n in nums:
            count=0
            for j in nums:
                if j<n:
                    count+=1
            ans.append(count)
        return ans
answer = Solution()
print(answer.smallerNumbersThanCurrent([1,5,4,3,6,7,4,0]))