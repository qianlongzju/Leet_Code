class ExamRoom(object):

    def __init__(self, N):
        """
        :type N: int
        """
        self.seats = []
        self.N = N

    def seat(self):
        """
        :rtype: int
        """
        #print self.seats
        n = len(self.seats)
        if n == 0:
            self.seats.append(0)
            return 0
        max_len = 0
        for i in range(1, n):
            a, b = self.seats[i], self.seats[i-1] 
            if (a-b)//2 > max_len:
                max_len = (a-b)//2
                index = (a+b)//2
        if self.N-1-self.seats[-1] > max_len:
            index = self.N-1
            max_len = self.N-1-self.seats[-1]
        if self.seats[0] - 0 >= max_len:
            index = 0
        for i in range(n):
            if self.seats[i] > index:
                self.seats.insert(i, index)
                break
        else:
            self.seats.append(index)
        return index

    def leave(self, p):
        """
        :type p: int
        :rtype: None
        """
        self.seats.remove(p)


# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(N)
# param_1 = obj.seat()
# obj.leave(p)
