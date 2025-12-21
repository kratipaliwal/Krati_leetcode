#from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #if you use just the counter
        #return Counter(s) == Counter(t)
        counter1,counter2 = {},{}
        for i in s: 
            if i in counter1:
                counter1[i] += 1
            else:
                counter1[i] = 1
        for j in t:
            if j in counter2:
                counter2[j] += 1
            else:
                counter2[j] = 1
        return (counter1 == counter2 )
