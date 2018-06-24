class MinStack:
    def __init__(self):
        self.data = []
        self.min = []
    # @param x, an integer
    # @return an integer
    def push(self, x):
        self.data.append(x)
        if len(self.min) > 0 and x > self.min[-1]:
            pass
        else:
           self.min.append(x)
        return x

    # @return nothing
    def pop(self):
        temp = self.data[-1]
        self.data.pop()
        if temp == self.min[-1]:
            self.min.pop()

    # @return an integer
    def top(self):
        return self.data[-1]

    # @return an integer
    def getMin(self):
        return self.min[-1]
