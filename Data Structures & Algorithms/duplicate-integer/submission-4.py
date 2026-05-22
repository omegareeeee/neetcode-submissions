class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        noDupes = {}

        for num in nums:
            if num in noDupes:
                return True
            else:
                noDupes[num] = 1
        return False


        