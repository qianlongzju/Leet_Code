class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        mapping_h = [[] for i in range(5)]
        mapping_m = [[] for i in range(7)]

        for i in range(12):
            count = 0
            ii = i
            while ii != 0:
                if ii & 0x01 == 1:
                    count += 1
                ii >>= 1
            mapping_h[count].append(i)
        for i in range(60):
            count = 0
            ii = i
            while ii != 0:
                if ii & 0x01 == 1:
                    count += 1
                ii >>= 1
            mapping_m[count].append(i)
        result = []
        for h in range(min(num + 1, 5)):
            m = num - h
            if m > 6:
                continue
            for hh in mapping_h[h]:
                for mm in mapping_m[m]:
                    result.append("%d:%02d" % (hh, mm))
        return result
        
