class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        stack = []
        d = {}
        for i in range(len(nums2)):
            x = nums2[i]
            if not stack:
                stack.append(x)
                continue
            if x < stack[-1]:
                stack.append(x)
                continue
            while stack and x > stack[-1]:
                k = stack.pop(-1)
                d[k] = x
            stack.append(x)
        return [d[n] if n in d else -1 for n in nums1]
