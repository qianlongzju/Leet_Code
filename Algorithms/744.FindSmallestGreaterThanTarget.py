class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        low, high = 0, len(letters)-1
        while low < high:
            mid = low + (high - low) / 2
            if ord(target) >= ord(letters[mid]):
                low = mid + 1
            else:
                high = mid
        if ord(letters[low]) > ord(target):
            return letters[low]
        if ord(letters[high]) <= ord(target):
            return letters[0]
        return letters[high]
