class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        windowSize = len(s1)

        if windowSize > len(s2):
            return False
        
        l = 0
        s1= "".join(sorted(s1))
        for r in range(windowSize-1, len(s2)):
            sub = "".join(sorted(s2[l : r+1]))
            if s1 in sub:
                return True
            l += 1
        return False