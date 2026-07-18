class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        longest = 0 
        counts = [0] * 26
        n = len(s)

        for r in range(n):
            counts[ord(s[r]) - 65] += 1
            #checking below if window is valid (elements we need to change > elements we are allowed to change)
            while (r-l+1) - max(counts) > k :
                #drop that element and move l ahead 
                counts[ord(s[l]) - 65] -= 1 
                l += 1 
            longest = max(longest, (r-l +1))
        return longest 

# you dont actually have to replace an element you just need to check it can be replaced. 