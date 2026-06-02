#TC : O(n)/O(mx)
#SC : O(mx)

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n=max(nums)+1
        freq=[0]*(n)
        for i in nums:
            freq[i]+=1
            
        nums.clear()

        for i in range(n):
            while freq[i]>0:
                nums.append(i)
                freq[i]-=1
        return nums

o = Solution()
print(o.sortArray([5,1,1,2,0,0]))
print(o.sortArray([5,2,3,1]))
