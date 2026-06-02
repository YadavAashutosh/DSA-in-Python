# BEST CASE / AVERAGE CASE : O(nlogn)
# WORST CASE: O(N^2)
# SPACE COMPLEXITY: O(1)

class Solution:
    def partition(self,nums,l,r):
        key = nums[r]
        start = l
        for i in range(l,r):
            if nums[i]<=key:
                temp=nums[i]
                nums[i]=nums[start]
                nums[start]=temp
                start+=1
        temp=nums[r]
        nums[r]=nums[start]
        nums[start]=temp
        return start


    def quicksort(self,nums,l,r):
        if l>=r:
            return 
        p=self.partition(nums,l,r)
        self.quicksort(nums,l,p-1)
        self.quicksort(nums,p+1,r)
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quicksort(nums,0,len(nums)-1)
        return nums


o = Solution()
print(o.sortArray([5,1,1,2,0,0]))
print(o.sortArray([5,2,3,1]))
print(o.sortArray([-1,2,-3,4,0]))
print(o.sortArray([1, 3, 6, 5, 3, 2, 235, 45, 567, 456, 345234, 123, 234, 3453456]))

# [0, 0, 1, 1, 2, 5]
# [1, 2, 3, 5]
# [-3, -1, 0, 2, 4]
# [1, 2, 3, 3, 5, 6, 45, 123, 234, 235, 456, 567, 345234, 3453456]