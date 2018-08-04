class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        l1, l2 = len(s1), len(s2)
        if l1 != l2:
            return False
        if l1 == 0:
            return True
        if l1 == 1:
            return s1 == s2
        ss1, ss2 = sorted(s1), sorted(s2)
        if ss1 != ss2:
            return False
        for i in range(1, l1):
            s11, s12 = s1[:i], s1[i:]
            s21, s22 = s2[:i], s2[i:]
            if self.isScramble(s11, s21) and self.isScramble(s12, s22):
                return True
            s23, s24 = s2[:l1-i], s2[l1-i:]
            if self.isScramble(s11, s24) and self.isScramble(s12, s23):
                return True
        return False
