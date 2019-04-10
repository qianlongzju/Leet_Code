class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        alphabets = [log for log in logs if not log.split()[1].isnumeric()]
        numerics = [log for log in logs if log.split()[1].isnumeric()]
        alphabets.sort(key=lambda x: " ".join(x.split()[1:]))
        return alphabets + numerics
