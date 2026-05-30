class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s: # counts the character
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s) # the key is a finger print for the word, 
                                        # then adds string
        return list(res.values()) #converts thte hash table values into list 
            #(k,v) -> (count finger print, group of anagrams)

        