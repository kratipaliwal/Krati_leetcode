class Solution:
    def binary_search(self, start: int, end: int, nums: List[int], target: int) -> int:
        if start > end:
            return - 1 
        m = (start + end) // 2
        if nums[m] == target:
            return m
        elif nums[m] > target:
            return self.binary_search(start,m-1,nums,target)
        return self.binary_search(m+1,end,nums,target)

    def search(self, nums: List[int], target: int) -> int:
        return self.binary_search(0, len(nums)-1, nums, target)
 



        