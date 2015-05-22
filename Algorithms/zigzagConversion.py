class Solution:
    # @param string s
    # @param integer numRows
    # @return string
    def convert(self, s, numRows):
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
