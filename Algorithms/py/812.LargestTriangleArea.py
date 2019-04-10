class Solution(object):
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        max_area = 0
        n = len(points)
        for i in range(n):
            p1 = points[i]
            for j in range(i+1, n):
                p2 = points[j]
                a = ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2) ** 0.5
                for k in range(j+1, n):
                    p3 = points[k]
                    b = ((p3[0]-p2[0])**2 + (p3[1]-p2[1])**2) ** 0.5
                    c = ((p1[0]-p3[0])**2 + (p1[1]-p3[1])**2) ** 0.5
                    if c <= abs(a-b) or c >= a+b:
                        continue
                    cos = (a**2 + b**2 - c**2)/(2*a*b)
                    area = 0.5*a*b*((1-cos**2)**0.5)
                    max_area = max(max_area, area)
        return max_area
