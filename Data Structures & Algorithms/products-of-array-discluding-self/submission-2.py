class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        preFix = [1] * len(nums)
        postFix = [1] * len(nums)

        pre = 1
        for i in range(len(nums)-1):
            preFix[i] = pre
            pre *= nums[i]
            preFix[i+1] = pre

        post = 1
        for i in range(len(nums)-1,0, -1):
            postFix[i] = post
            post *= nums[i]
            postFix[i-1] = post

        res = [1] * len(nums)
        for i in range(len(nums)):
            res[i] = preFix[i] *  postFix[i]

        return res
