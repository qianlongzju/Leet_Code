__author__ = 'qianlong'
class Solution:
    # @param num, a list of integers
    # @return an integer
    def majorityElement(self, num):
        previous = None
        count = 0
        for current in num:
            if count == 0:
                previous = current
                count += 1
            else:
                if current == previous:
                    count += 1
                else:
                    count -= 1
        return previous
