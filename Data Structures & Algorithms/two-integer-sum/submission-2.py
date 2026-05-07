class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index = {}

        for i, n in enumerate(nums):
            index[n] = i

        for i, n in enumerate(nums):
            dif = target - nums[i]
            if dif in index and index[dif] != i:
                return [i,index[dif]]
            

            

        