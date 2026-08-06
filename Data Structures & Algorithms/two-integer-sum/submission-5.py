class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffs = defaultdict(int) #key = difference of  value = index

        for i in range(len(nums)):
            twoSum = target - nums[i]
            if twoSum in diffs.keys():
                return [diffs[twoSum], i]
            else:
                diffs[nums[i]] = i

        return [6,7]
        