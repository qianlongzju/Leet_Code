class Solution(object):
    def minAreaFreeRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        points = [tuple(point) for point in points]
        p = set(points)
        n = len(points)
        area = None
        for i in range(n):
            p1 = points[i]
            for j in range(n):
                if j == i:
                    continue
                p2 = points[j]
                for k in range(n):
                    if k == i or k == j:
                        continue
                    p3 = points[k]
                    p4 = (p2[0] + p3[0] - p1[0], p2[1] + p3[1] - p1[1])
                    if p4 not in p:
                        continue
                    p21 = (p2[0] - p1[0], p2[1] - p1[1])
                    p31 = (p3[0] - p1[0], p3[1] - p1[1])
                    if p21[0] * p31[0] + p21[1] * p31[1] != 0:
                        continue
                    print p21, p31
                    if area == None:
                        area = (p21[0]**2 + p21[1]**2) * (p31[0]**2 + p31[1]**2)
                    else:
                        area = min(area, (p21[0]**2 + p21[1]**2) * (p31[0]**2 + p31[1]**2))
        if area == None:
            return 0
        return math.sqrt(area)
