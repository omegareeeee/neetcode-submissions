class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index = {}

        for i, n in enumerate(nums):
            dif = target - n
            if dif in index:
                return [index[dif],i]
            index[n] = i
            

            

        