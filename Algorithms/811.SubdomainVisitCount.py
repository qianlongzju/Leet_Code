class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        import collections
        count = collections.defaultdict(int)
        for cpdomain in cpdomains:
            c, domain = cpdomain.split()
            parts = domain.split(".")
            for i in range(len(parts)):
                count[".".join(parts[i:])] += int(c)
        return [str(v) + " " + k for k, v in count.items()]
