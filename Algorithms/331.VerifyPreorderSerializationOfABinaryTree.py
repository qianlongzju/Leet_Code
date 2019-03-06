class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        count = -1
        for v in preorder.split(","):
            count += 1
            if count > 0:
                return False
            if v != '#':
                count -= 2
        return count == 0
