class Solution(object):
    def strWithout3a3b(self, A, B):
        """
        :type A: int
        :type B: int
        :rtype: str
        """
        flag = False
        if A > B:
            flag = True
            A, B = B, A
        result = ""
        while B > A and A > 0:
            result += "bba"
            B -= 2
            A -= 1
        if A == B:
            while A > 0:
                result += "ba"
                A -= 1
                B -= 1
        if A == 0:
            while B > 0:
                result += "b"
                B -= 1
        if flag:
            result = result.replace("a", "c").replace("b", "a").replace("c", "b")
        return result
