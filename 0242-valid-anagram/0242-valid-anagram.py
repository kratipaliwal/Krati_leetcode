class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        else: 
            counts1 =  {}
            counts2 = {}
            for i in range(0,len(s)):
                counts1[s[i]] = 1 + counts1.get(s[i],0)
                counts2[t[i]] = 1 + counts2.get(t[i],0)
            return counts1 == counts2