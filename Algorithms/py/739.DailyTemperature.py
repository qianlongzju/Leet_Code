class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        stack = []
        result = [0] * len(T)
        for i in range(len(T)):
            if not stack or T[i] <= T[stack[-1]]:
                stack.append(i)
            else:
                while stack and T[i] > T[stack[-1]]:
                    t = stack.pop()
                    result[t] = i - t
                stack.append(i)
        return result
