class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        scores = []
        for op in ops:
            if op == '+':
                scores.append(scores[-1] + scores[-2])
            elif op == 'D':
                scores.append(2 * scores[-1])
            elif op == 'C':
                scores.pop(-1)
            else:
                scores.append(int(op))
        return sum(scores)