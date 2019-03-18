class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        import collections
        count = 0
        n = len(points)
        for i in range(n):
            p1 = points[i]
            d = collections.defaultdict(int)
            for j in range(n):
                if j == i:
                    continue
                p2 = points[j]
                dist = (p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2
                d[dist] += 1
            for k, v in d.items():
                if v > 1:
                    count += v*(v-1)
        return count
