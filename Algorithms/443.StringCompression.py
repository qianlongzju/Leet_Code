class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        i = 0
        j = 1
        count = 1
        while j < len(chars):
            if chars[i] == chars[j]:
                count += 1
            else:
                if count != 1:
                    for d in str(count):
                        i += 1
                        chars[i] = d
                i += 1
                chars[i] = chars[j]
                count = 1
            j += 1
        else:
            if count != 1:
                for d in str(count):
                    i += 1
                    chars[i] = d
        return i+1
