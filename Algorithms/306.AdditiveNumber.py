class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        for i in range(1, len(num)):
            a = num[:i]
            if a != '0' and a.startswith('0'):
                continue
            if 2 * i + 1 > len(num):
                break
            for j in range(i+1, len(num)):
                b = num[i:j]
                if b != '0' and b.startswith('0'):
                    continue
                if len(a) + len(b) + max(len(a), len(b)) > len(num):
                    break
                aa, bb = int(a), int(b)
                c = aa + bb
                k = j
                while k < len(num):
                    if not num[k:].startswith(str(c)):
                        break
                    k += len(str(c))
                    aa, bb = bb, c
                    c = aa + bb
                if k == len(num):
                    return True
        return False
