class Solution:
    def ispalindrome(self,x : int)->bool:
        if x<0:
            return False
        y = list(map(int,str(x)))
        m=1
        for i in range(len(y)//2):
            if y[i]!=y[-m]:
                return False
            m+=1
        return True
ans = Solution()
print(ans.ispalindrome(121))
print(ans.ispalindrome(-121))
print(ans.ispalindrome(10))


'''
Best way 

class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        return s == s[::-1]
        # if s[::-1] != s:
        #     return False
        # return True

Or 

class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp = x
        rev = 0

        while temp > 0:
            r = temp % 10
            temp //= 10
            rev = rev * 10 + r

        return rev == x
'''