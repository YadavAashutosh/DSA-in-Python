class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dict1={}
        for i in range(len(numbers)):
            rem =  target - numbers[i]
            if rem in dict1 :
                return [dict1[rem],i+1]

            dict1[numbers[i]]=i+1
lists = Solution()
print(lists.twoSum([2,7,11,15],9))
print(lists.twoSum([3,2,4],6))
print(lists.twoSum([-1,0],-1))
# [1, 2]
# [2, 3]
# [1, 2]