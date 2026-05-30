class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n==0:
            return 0     
        set1 = set()
        set1.add(s[0])
        ans = 1
        i = 0
        j=1
        while j<n:
            while s[j] in set1:
                set1.discard(s[i])
                i+=1
            set1.add(s[j])
            j+=1
            ans = max(ans , j-i)
        return ans
o=Solution()
print(o.lengthOfLongestSubstring("abcabcbb"))
print(o.lengthOfLongestSubstring("bbbbb"))
print(o.lengthOfLongestSubstring( "pwwkew"))
print(o.lengthOfLongestSubstring( "dvdf"))

# 3
# 1
# 3
# 3


# below code is correct in some cases only

'''class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        set1=set()
        count=0
        maxcount=1
        for i in range(len(s)):
            if s[i] not in set1:
                set1.add(s[i])
                count+=1
                if count>maxcount:
                    maxcount=count
            else:
                set1.clear()
                count=1
                set1.add(s[i])
        return maxcount
o=Solution()
print(o.lengthOfLongestSubstring("abcabcbb"))
print(o.lengthOfLongestSubstring("bbbbb"))
print(o.lengthOfLongestSubstring( "pwwkew"))
print(o.lengthOfLongestSubstring( "dvdf"))#wrong here 
# 3
# 1
# 3
# 2 here it should be 3
'''