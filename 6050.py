# https://leetcode-cn.com/problems/total-appeal-of-a-string/solution/by-endlesscheng-g405/
class Solution(object):
    def appealSum(self, s):
        """
        :type s: str
        :rtype: int
        """
        res, cur_s, pos = 0, 0, [-1] * 26
        for i, c in enumerate(s):
            t = ord(c) - ord('a')
            cur_s += i - pos[t]
            res += cur_s
            pos[t] = i
        return res

#class Solution(object):
#    def appealSum(self, s):
#        """
#        :type s: str
#        :rtype: int
#        """
#        res = 0
#        data = {}
#        d = 1
#        i = 0
#        while i < len(s):
#            j = i-1
#            d = 1
#            while True:
#                j += d
#                if j >= len(s):
#                    j -= d
#                    data[s[i]] -= 1
#                    if data[s[i]] == 0:
#                        del data[s[i]]
#                    i += 1
#                    d = -1
#                if j < i:
#                    i += 1
#                    break         
#                if d > 0 and s[j] not in data:
#                    data[s[j]] = 0
#                if d > 0:
#                    data[s[j]] += d
#
#                #print(i, j, len(data), data)
#                res += len(data)
#                if d < 0:
#                    data[s[j]] += d
#                if data[s[j]] == 0:
#                    del data[s[j]]
#            #print(res)
#            #print('a', i, j, data)
#        return res
