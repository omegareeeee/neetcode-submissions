class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        chars1 = [0] * 26
        chars2 = [0] * 26

        for n in range(len(s)):
            val = ord(s[n]) - ord('a')
            chars1[val] += 1
            val = ord(t[n]) - ord('a')
            chars2[val] += 1
        
        return chars1 == chars2
    