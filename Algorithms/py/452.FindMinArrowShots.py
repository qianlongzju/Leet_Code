class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        ans = 1
        prev = 0
        for i in range(1, len(points)):
            point = points[i]
            if point[0] > points[prev][1]:
                ans += 1
                prev = i     
        return ans