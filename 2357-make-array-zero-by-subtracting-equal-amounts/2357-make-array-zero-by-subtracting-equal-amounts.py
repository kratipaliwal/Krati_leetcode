class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        distinct = set()
        for i in nums:
            if i != 0:  
                distinct.add(i)
        return len(distinct)


        # Brute force 
        # passes = 0
        # # in python 0 is false, rest is true. 
        # while any(nums): 
        #     x = min(n for n in nums if n>0)
        #     for i in range(len(nums)):
        #         if nums[i] > 0:
        #             nums[i] -= x 
        #     passes += 1 
        # return passes