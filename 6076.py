class Solution(object):
    def minimumLines(self, stockPrices):
        """
        :type stockPrices: List[List[int]]
        :rtype: int
        """
        stockPrices = sorted(stockPrices)
        def on_one_line(point, line):
            x, y = point
            point1, point2 = line
            x1, y1 = point1
            x2, y2 = point2
            if (y-y1)*(x-x2) == (y-y2)*(x-x1):
                return True
            return False
        if len(stockPrices) <= 1:
            return 0
        if len(stockPrices) == 2:
            return 1
        line_num = 1
        line = [stockPrices[0], stockPrices[1]]
        for i in range(2, len(stockPrices)):
            if not on_one_line(stockPrices[i], line):
                line = [stockPrices[i-1], stockPrices[i]]
                line_num += 1
        return line_num
                
