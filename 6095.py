class Solution(object):
    def strongPasswordCheckerII(self, password):
        """
        :type password: str
        :rtype: bool
        """
        if len(password) < 8: return False
        lower, upper, digit, sp = False, False, False, False
        pre = None
        for c in password:
            if c in string.ascii_lowercase:
                lower = True
            elif c in string.ascii_uppercase:
                upper = True
            elif c in string.digits:
                digit = True
            elif c in '!@#$%^&*()-+':
                sp = True
            if pre and c == pre:
                return False
            pre = c
        return lower and upper and digit and sp
                
