class Solution:
    # @param string s
    # @param integer numRows
    # @return string
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        result = [[] for i in range(numRows)]
        i, j = 0, 0
        direction = 0
        for k in range(len(s)):
            result[i].append(s[k])
            if direction == 0:
                i += 1
            else:
                i -= 1
                j += 1
            if i == numRows-1:
                direction = 1
            elif i == 0:
                direction = 0
        return "".join(["".join(row) for row in result])

    def convert_1(self, s, numRows):
        if numRows == 1: 
            return s
        result = ""
        offset = 2 * (numRows - 1)
        for i in range(numRows):
            if i == 0 or i == numRows-1:
                j = 0
                while i+j*offset < len(s):
                    result += s[i + offset * j]
                    j += 1
            else:
                odd = False
                j = 0
                while True:
                    if odd:
                        if i+(offset)*(j+1)/2-2*i >= len(s):
                            break
                        result += s[i+(offset)*(j+1)/2-2*i]
                    else:
                        if i+offset*(j/2) >= len(s):
                            break
                        result += s[i+offset*(j/2)]
                    odd = not odd
                    j += 1
        return result
