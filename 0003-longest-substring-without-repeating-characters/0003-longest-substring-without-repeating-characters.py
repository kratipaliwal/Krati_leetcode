class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sett = set()
        l = 0 
        n = len(s)
        longest = 0

        for r in range(n):
            while s[r] in sett:
                sett.remove(s[l])
                l += 1
        
            win = (r-l) + 1 
            longest = max(longest,win)
            sett.add(s[r])
    
        return longest 


        