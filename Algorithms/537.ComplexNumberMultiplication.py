class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        def help(s):
            return map(int, s[:-1].split("+"))
        ai, aj = help(a)
        bi, bj = help(b)
        return str(ai*bi-aj*bj)+"+"+str(ai*bj+bi*aj) + "i"
