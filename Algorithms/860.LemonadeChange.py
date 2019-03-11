class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        count_5, count_10 = 0, 0
        for bill in bills:
            if bill == 5:
                count_5 += 1
            elif bill == 10:
                count_5 -= 1
                count_10 += 1
            else:
                if count_10 == 0:
                    count_5 -= 3
                else:
                    count_10 -= 1
                    count_5 -= 1
            if count_5 < 0:
                return False
        return True
