class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        def gcd(a, b):
            if b == 0:
                return a
            return gcd(b, a % b)
        size = len(points)
        if size <= 2:
            return size
        slopeMap = collections.defaultdict(int)
        maxCount = 0
        for i in range(size):
            duplicates, vertical = 1, 0
            slopeMap.clear()
            for j in range(size):
                if i == j:
                    continue
                if points[i].x == points[j].x and points[i].y == points[j].y:
                    duplicates += 1
                    continue
                if points[i].x == points[j].x:
                    vertical += 1
                    continue
                dy, dx = points[i].y - points[j].y, points[i].x - points[j].x
                d = gcd(dy, dx)
                slopeMap[dx / d, dy / d] += 1
            if slopeMap:
                vertical = max(vertical, max(slopeMap.values()))
            maxCount = max(vertical + duplicates, maxCount)
        return maxCount
