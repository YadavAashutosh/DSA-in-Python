class Solution:
    def countn(self ,num :int)->int:
        count=0
        n=num
        while n>0:
            r=n%10
            if num%r==0:
                count+=1
            n//=10
        return count
answer = Solution()
print(answer.countn(7))
print(answer.countn(121))
print(answer.countn(1248))

# Another method
# class Solution:
#     def countDigits(self, num: int) -> int:
#         count = 0
#         n = list(map(int, str(num)))

#         for i in n:
#             if num%i==0:
#                 count+=1
#         return count
    