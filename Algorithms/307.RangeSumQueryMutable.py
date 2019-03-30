# https://www.youtube.com/watch?v=Oq2E2yGadnU
# https://blog.csdn.net/Yaokai_AssultMaster/article/details/79599809
class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.BIT = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            self.init(i + 1, nums[i])

    def init(self, i, val):
        while i < len(self.BIT):
            self.BIT[i] += val
            i = i + (i & -i)

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: None
        """
        delta = val - self.nums[i]
        self.nums[i] = val
        self.init(i + 1, delta)

    def getSum(self, i):
        s = 0
        while i > 0:
            s += self.BIT[i]
            i = i - (i & -i)
        return s

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.getSum(j + 1) - self.getSum(i);

class SegmentTreeNode(object):
    def __init__(self, start, end, s, left=None, right=None):
        self.start = start
        self.end = end
        self.s = s
        self.left = left
        self.right = right

class NumArray_tree(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.root = self.build_tree(0, len(nums)-1, nums)

    def build_tree(self, start, end, nums):
        if start > end:
            return None
        if start == end:
            return SegmentTreeNode(start, end, nums[start])
        mid = (start + end) // 2
        left = self.build_tree(start, mid, nums)
        right = self.build_tree(mid+1, end, nums)
        return SegmentTreeNode(start, end, left.s+right.s, left, right)

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: None
        """
        self.update_tree(self.root, i, val)

    def update_tree(self, node, i, val):
        if node.start == node.end == i:
            node.s = val
            return
        mid = (node.start + node.end) // 2
        if i <= mid:
            self.update_tree(node.left, i, val)
        else:
            self.update_tree(node.right, i, val)
        node.s = node.left.s + node.right.s

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.sumRange_tree(self.root, i, j)

    def sumRange_tree(self, node, i, j):
        if node.start == i and node.end == j:
            return node.s
        mid = (node.start + node.end) // 2
        if j <= mid:
            return self.sumRange_tree(node.left, i, j)
        elif i > mid:
            return self.sumRange_tree(node.right, i, j)
        else:
            return self.sumRange_tree(node.left, i, mid) + self.sumRange_tree(node.right, mid+1, j)


class NumArray_array(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.n = len(nums)
        self.sumSegmentTree = [0] * self.n + nums
        for i in range(self.n-1, 0, -1):
            self.sumSegmentTree[i] = self.sumSegmentTree[2*i] + self.sumSegmentTree[2*i+1]

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: None
        """
        i += self.n
        self.sumSegmentTree[i] = val
        while i > 1:
            i >>= 1
            self.sumSegmentTree[i] = self.sumSegmentTree[2*i] + self.sumSegmentTree[2*i+1]

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        i, j = i+self.n, j+self.n+1
        s = 0
        while i < j:
            if i & 0x01 == 1:
                s += self.sumSegmentTree[i]
                i += 1
            if j & 0x01 == 1:
                j -= 1
                s += self.sumSegmentTree[j]
            i >>= 1
            j >>= 1
        return s


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)
