class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]
        index = 0
        for i in range(len(strs[0])):
            flag = True
            for j in range(1, len(strs)):
                if i < len(strs[j]) and strs[0][i] == strs[j][i]:
                    continue
                else:
                    flag = False
            if not flag:
                break
            index = i+1
        return strs[0][:index]
