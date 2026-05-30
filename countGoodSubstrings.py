class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        
        count = 0
        for i in range(0,len(s)-2):
            if s[i]==s[i+1] or s[i]==s[i+2] or s[i+1]==s[i+2]:
                pass
            else:
                count +=1
        return count


o = Solution()
print(o.countGoodSubstrings("xyzzaz"))
print(o.countGoodSubstrings("aababcabc"))

# 1
# 4