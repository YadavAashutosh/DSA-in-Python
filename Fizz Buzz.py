class Solution:
    def fb(self,n: int) -> List[str]:
        ans= []
        for i in range (1,n+1):
            if i%3==0 and i%5==0:
                ans.append("FizzBuzz")
            elif i%3==0:
                ans.append("Fizz")
            elif i%5==0:
                ans.append("Buzz")
            else :
                ans.append(str(i)) 
        return ans

a=Solution()
a.fb(10)  # No output here because return doesnt print anything it just fetch the value 
# def hello():
#     print("Hi")

# x = hello() here the value of x is None
# print(x) here it will print hi and None bcuz no return value


print(a.fb(15))
