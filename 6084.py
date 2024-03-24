class Solution(object):
    def largestWordCount(self, messages, senders):
        """
        :type messages: List[str]
        :type senders: List[str]
        :rtype: str
        """
        d = {}
        for msg, sender in zip(messages, senders):
            if sender not in d:
                d[sender] = 0
            d[sender] += len(msg.split(" "))
        result = sorted(d.items(), key=lambda x: (x[1], x[0]))
        #print(result)
        return result[-1][0]
            
