class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.split()
        i=0
        j=len(s)-1
        while i<j:
            temp=s[i]
            s[i]=s[j]
            s[j]=temp
            i+=1
            j-=1
        return " ".join(s)
ans = Solution()
print(ans.reverseWords("the sky is blue"))
print(ans.reverseWords("  hello world  "))
print(ans.reverseWords( "a good   example"))

# blue is sky the
# world hello
# example good a

    
    