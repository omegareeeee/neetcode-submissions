class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        unqiue = set()
        res = 0
        
        for r in range(len(s)):
            while s[r] in unqiue:
                unqiue.remove(s[l])
                l += 1
            unqiue.add(s[r])
            res = max(res, r-l +1)
        
        return res

    #something a lil weird wit da counter fr

        