class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sorted_s = sorted(s)
        sorted_t = sorted(t)
        for n in range(len(s)):
            if sorted_s[n] != sorted_t[n]:
                return False
        return True
    