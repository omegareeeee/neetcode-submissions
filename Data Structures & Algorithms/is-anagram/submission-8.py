class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False
        charCount = {}
        length = len(s)
        for i in range(length):
            if s[i] in charCount:
                charCount[s[i]] += 1
            else:
                charCount[s[i]] = charCount.get(s[i], 0) + 1

        charCount2 = {}
        for i in range(length):
            if t[i] in charCount2:
                charCount2[t[i]] += 1
            else:
                charCount2[t[i]] = charCount2.get(t[i], 0) + 1
        
        return charCount == charCount2


        