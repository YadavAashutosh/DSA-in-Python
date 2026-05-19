class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n==0:
            return 1
        if n<0:
            return self.myPow(1/x,-n)
        a = self.myPow(x,n//2)
        if n%2==0:
            return a*a
        return a*a*x
b=Solution()
print(b.myPow(2.0,10))
print(b.myPow(2.1,3))
print(b.myPow(2.0,-2))