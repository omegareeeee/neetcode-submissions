class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1
        maxHeight = 0

        while l < r:
            minHeight = min(heights[r], heights[l])
            curArea = (r - l) * minHeight
            maxHeight = max(maxHeight, curArea)

            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1

        return maxHeight
        