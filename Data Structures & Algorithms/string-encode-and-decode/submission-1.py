class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_strs = ""
        for word in strs:
            encoded_strs += str(len(word)) + "#" + word
        return encoded_strs

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        j = 0
        while j < len(s):
            if s[j] == "#":
                length = int(s[i:j])
                i = j + 1
                j += length
                res.append(s[i:j+1])
                i = j + 1
                j = i + 1
            else:
                j += 1

        return res


        

