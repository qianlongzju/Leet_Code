class Solution(object):
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        i = 0
        mask0 = 1 << 7
        mask2 = 1 << 6
        while i < len(data):
            num = data[i]
            if num & mask0 == 0:
                i += 1
                continue
            mask1 = 1 << 7
            n_bytes = 0
            while mask1 & num:
                n_bytes += 1
                mask1 >>= 1
            if n_bytes > 4 or n_bytes == 1:
                return False
            while n_bytes > 1:
                n_bytes -= 1
                i += 1
                if i >= len(data):
                    return False
                num = data[i]
                if not (num & mask0 and not (num & mask2)):
                    return False
            i += 1
        return True
