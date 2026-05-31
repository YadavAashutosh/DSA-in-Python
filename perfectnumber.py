class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num==1:
            return False
        n=1
        for i in range (2,int(num**0.5)+1):
            if num%i==0:
                n+=i
                if num//i!=i:
                    n+=num//i
        return n==num
o=Solution()
print(o.checkPerfectNumber(28))
print(o.checkPerfectNumber(7))
print(o.checkPerfectNumber(6))

# True
# False
# True