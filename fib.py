class Solution:
    def fib(self, n: int) -> int:
        if n==0 or n==1:
            return n
        return self.fib(n-1) + self.fib(n-2)
        
a = Solution()
print(a.fib(1))
print(a.fib(2))
print(a.fib(3))
print(a.fib(4))
print(a.fib(5))