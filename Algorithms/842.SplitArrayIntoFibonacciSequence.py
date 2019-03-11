class Solution(object):
    def splitIntoFibonacci(self, num):
        """
        :type S: str
        :rtype: List[int]
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
                result = [aa, bb]
                k = j
                while k < len(num):
                    if c > 2**31 - 1:
                        break
                    if not num[k:].startswith(str(c)):
                        break
                    result.append(c)
                    k += len(str(c))
                    aa, bb = bb, c
                    c = aa + bb
                if k == len(num):
                    print "".join([str(r) for r in result]) == num
                    return result
        return []
