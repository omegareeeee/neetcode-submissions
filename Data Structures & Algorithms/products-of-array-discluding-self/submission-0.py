class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        i = 0
        while i < len(nums):
            j = 0
            while j < len(nums):
                if i != j:
                    res[i] *= nums[j]
                j += 1
            i += 1

        return res
            