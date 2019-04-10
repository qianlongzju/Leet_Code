class Solution(object):

    def __init__(self, n_rows, n_cols):
        """
        :type n_rows: int
        :type n_cols: int
        """
        self.n_rows = n_rows
        self.n_cols = n_cols
        self.set = set()

    def flip(self):
        """
        :rtype: List[int]
        """
        import random
        x = random.randint(0, self.n_rows * self.n_cols - 1)
        while x in self.set:
            x = random.randint(0, self.n_rows * self.n_cols - 1)
        self.set.add(x)
        return x / self.n_cols, x % self.n_cols
        

    def reset(self):
        """
        :rtype: void
        """
        self.set.clear()


# Your Solution object will be instantiated and called as such:
# obj = Solution(n_rows, n_cols)
# param_1 = obj.flip()
# obj.reset()
