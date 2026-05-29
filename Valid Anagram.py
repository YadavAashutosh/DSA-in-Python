class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        freq = {}

        for ch in s:

            if ch not in freq:
                freq[ch] = 1
            else:
                freq[ch] += 1

        for ch in t:

            if ch not in freq:
                return False

            freq[ch] -= 1

        for i in freq.values():
            if i!=0:
                return False

        return True
    

o = Solution()

print(o.isAnagram("anagram", "nagaram")) #true
print(o.isAnagram("rat", "car"))#false