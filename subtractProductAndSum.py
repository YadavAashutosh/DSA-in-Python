class Solution:
    def subtractProductAndSum(self,n : int)->int:
        a = list(map(int,str(n)))
        b = 1
        c = 0 

        for i in a:
            b *= i
            c += i
        
        return b-c

ans = Solution()
print(ans.subtractProductAndSum(234)) #15
print(ans.subtractProductAndSum(4421)) #21

'''
Another method :

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        temp = n
        sum_ = 0
        product = 1

        while temp>0:
            r = temp%10
            temp//=10
            sum_+=r
            product*=r

        return product-sum_

'''