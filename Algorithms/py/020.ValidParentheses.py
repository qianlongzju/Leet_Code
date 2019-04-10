class Solution:
    # @return a boolean
    def isValid(self, s):
        mapping = {'(':')', '[':']', '{':'}'}
        stk = []
        for c in s:
            if c in mapping:
                stk.append(c)
            else:
                if not stk or mapping[stk.pop()] != c: return False
        return not stk
