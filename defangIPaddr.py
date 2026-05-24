class Solution(object):
    def defangIPaddr(self, address):
        s = ""
        for i in address:
            if i == ".":
                s += "[.]"
            else:
                s += i
        return s
        
ans=Solution()
print(ans.defangIPaddr("255.100.50.0"))#255[.]100[.]50[.]0