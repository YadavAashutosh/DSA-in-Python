class Solution:
    def sortedkey(self,s):
        s=sorted(s)
        return "".join(s)
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict1={}
        for i in strs:
            a = self.sortedkey(i)
            if a in dict1.keys():
                dict1[a].append(i)
            else :
                dict1.update({a:[i]})
        return list(dict1.values())
        
o = Solution()

print(o.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
print(o.groupAnagrams([""]))
print(o.groupAnagrams(["a"]))

# [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
# [['']]
# [['a']] 