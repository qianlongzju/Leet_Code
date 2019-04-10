class Solution(object):
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        line_no = 0
        cur_line = 0
        for c in S:
            n = widths[ord(c)-ord('a')]
            if cur_line + n > 100:
                line_no += 1
                cur_line = n
            else:
                cur_line += n
        if cur_line > 0:
            line_no += 1
        return [line_no, cur_line]
