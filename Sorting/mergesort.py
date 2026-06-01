
# TIME COMPLEXITY: O(nlogn)
# SPACE COMPLEXITY: O(n)

class Solution:
    def merge(self , nums,l ,mid,r):
        a=[]
        b=[]
        for i in range(l,mid+1):
            a.append(nums[i])
        for j in range(mid+1,r+1):
            b.append(nums[j])
        i,j,k = 0,0,l
        while k<=r:
            if j==len(b):
                nums[k]=a[i]
                i+=1
            elif i==len(a):
                nums[k]=b[j]
                j+=1
            elif a[i]<=b[j]:
                nums[k]=a[i]
                i+=1
            else :
                nums[k]=b[j]
                j+=1
            k+=1

    def mergesort(self,nums,l,r):
        if l>=r:
            return
        mid = (l+r)//2
        self.mergesort(nums,l,mid)
        self.mergesort(nums,mid+1,r)
        self.merge(nums,l,mid,r)
    def sortArray(self, nums: List[int]) -> List[int]:
        self.mergesort(nums,0,len(nums)-1)
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