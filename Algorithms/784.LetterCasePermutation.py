class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        self.result = []
        self.helper(S, 0, "")
        return self.result
    
    def helper(self, S, i, pre):
        if i > len(S):
            return
        if i == len(S):
            self.result.append(pre)
            return
        if S[i] in "0123456789":
            self.helper(S, i + 1, pre + S[i])
            return
        self.helper(S, i + 1, pre + S[i].lower())
        self.helper(S, i + 1, pre + S[i].upper())
