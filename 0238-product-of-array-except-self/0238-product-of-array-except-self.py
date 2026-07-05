class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)

        answer = [1] * l
        prefix = [1] * l
        suffix = [1] * l

        suffix[l - 1] = 1
        prefix[0] = 1

        for i in range(l - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]

        for i in range(1, l):
            prefix[i] = prefix[i - 1] * nums[i - 1]

        for i in range(l):
            answer[i] = prefix[i] * suffix[i]

        return answer