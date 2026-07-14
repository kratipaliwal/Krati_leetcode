class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        #using bucket sort 

        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        #calculate frequency of each element in input array 
        for n in nums: 
            count[n] = count.get(n,0) + 1 
        
        #insert into buckets basec on freq
        for n,c in count.items():
            freq[c].append(n)

        #insertion into result array 
        res = []
        for i in range(len(freq)-1, 0 , -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k: 
                    return res 

        