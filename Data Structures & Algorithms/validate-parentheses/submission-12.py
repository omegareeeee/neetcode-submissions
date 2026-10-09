class Solution:
    def isValid(self, s: str) -> bool:
        close_to_open = {"}":"{", "]":"[", ")":"("}

        stk = []

        for c in s:
            if stk and c in close_to_open: # if any contains
                if stk[-1] == close_to_open[c]:
                    stk.pop()
                else:
                    return False
            else:
                stk.append(c)
        

        return True if len(stk) == 0 else False

        