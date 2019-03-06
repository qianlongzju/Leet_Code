class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        stack_S = self.backspace(S)
        stack_T = self.backspace(T)
        if len(stack_S) != len(stack_T):
            return False
        for a, b in zip(stack_S, stack_T):
            if a != b:
                return False
        return True
        
    def backspace(self, S):
        stack = []
        for c in S:
            if c == '#':
                if stack:
                    stack.pop(-1)
            else:
                stack.append(c)
        return stack
