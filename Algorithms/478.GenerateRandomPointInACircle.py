class Solution(object):

    def __init__(self, radius, x_center, y_center):
        """
        :type radius: float
        :type x_center: float
        :type y_center: float
        """
        self.radius = radius
        self.x_center = x_center
        self.y_center = y_center

    def randPoint(self):
        """
        :rtype: List[float]
        """
        import random
        x_delta = random.uniform(-self.radius, self.radius)
        y_delta = random.uniform(-self.radius, self.radius)
        while x_delta*x_delta + y_delta*y_delta > self.radius*self.radius:
            x_delta = random.uniform(-self.radius, self.radius)
            y_delta = random.uniform(-self.radius, self.radius)
        return self.x_center + x_delta, self.y_center + y_delta

# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()
