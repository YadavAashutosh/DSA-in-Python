class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s.split()
        l=len(s)-1
        return len(s[l])
ans = Solution()
print(ans.lengthOfLastWord("Hello World"))#5
print(ans.lengthOfLastWord("   fly me   to   the moon  "))#4
print(ans.lengthOfLastWord("luffy is still joyboy"))#6