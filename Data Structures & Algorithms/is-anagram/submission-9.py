class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False
        charCount = {}
        length = len(s)
        for i in range(length):
            charCount[s[i]] = charCount.get(s[i], 0) + 1
            charCount[t[i]] = charCount.get(t[i], 0) - 1
        
        for key, value in charCount.items():
            if value != 0:
                return False
        
        return True


        