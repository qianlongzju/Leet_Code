class MyCalendarTwo(object):

    def __init__(self):
        self.calendars = []
        self.orders = []

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        for order in self.orders:
            if not (start >= order[1] or end <= order[0]):
                return False
        for cal in self.calendars:
            if not (start >= cal[1] or end <= cal[0]):
                i, j = max(start, cal[0]), min(end, cal[1])
                if i < j:
                    self.orders.append([i, j])
        self.calendars.append([start, end])
        return True
    
    
# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)
