class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        def check(n):
            d = set(str(n))
            if '0' in d:
                return False
            digits = [int(c) for c in d]
            return all(n%d == 0 for d in digits)
        return [i for i in range(left, right+1) if check(i)]
