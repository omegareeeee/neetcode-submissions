class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        wordCount = collections.defaultdict(str)

        for i in range(len(s)):
            wordCount[s[i]] = wordCount.get(s[i], 0) + 1
            wordCount[t[i]] = wordCount.get(t[i], 0) - 1

        for count in wordCount.values():
            if count != 0:
                return False

        return True
        