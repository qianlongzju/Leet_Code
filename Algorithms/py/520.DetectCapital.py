class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if len(word) <= 1:
            return True
        if word[0].isupper() and word[1].isupper():
            flag = 1
        elif word[0].islower() and word[1].islower():
            flag = 2
        elif word[0].isupper() and word[1].islower():
            flag = 3
        else:
            return False
        for i in range(1, len(word)):
            if flag == 1 and not word[i].isupper():
                return False
            elif (flag != 1) and word[i].isupper():
                return False
        return True
