class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        count = [0] * 26
        for task in tasks:
            count[ord(task) - ord('A')] += 1
        count.sort(reverse=True)
        c = 1
        for i in range(1, len(count)):
            if count[i] == count[0]:
                c += 1
        return max(len(tasks), (n+1) * (count[0]-1) + c)
