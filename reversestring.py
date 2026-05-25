class Solution:
    def reverseString(self, s: List[str]) -> None:
       i=0
       j=len(s)-1
       while i<j:
           temp=s[i]
           s[i]=s[j]
           s[j]=temp
           i+=1
           j-=1
       return s
ans = Solution()
print(ans.reverseString(["h","e","l","l","o"]))
print(ans.reverseString(["H","a","n","n","a","h"]))