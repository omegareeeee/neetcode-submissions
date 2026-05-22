class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) -1
        while l < r:
            currR =r
            while l < r:
                dif = target - numbers[l]
                if dif == numbers[r]:
                    return [l+1, r+1]
                r -= 1
                
            l += 1
            r = len(numbers) - 1
            
            
        return [0, 0]
        