class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.cnt = 1
        self.freq = 1
        self.left = None
        self.right = None
        
class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.root = None
        for n in nums:
            self.root = self.insertBST(n)

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        self.root = self.insertBST(val)
        return self.searchBST(val)
    
    def insertBST(self, val):
        new_node = TreeNode(val)
        node = self.root
        if node == None:
            return new_node
        while node:
            node.cnt += 1
            if val > node.val:
                if node.right == None:
                    node.right = new_node
                    break
                else:
                    node = node.right
            elif val < node.val:
                if node.left == None:
                    node.left = new_node
                    break
                else:
                    node = node.left
            else:
                node.freq += 1
                break
        return self.root
    
    def searchBST(self, val):
        node = self.root
        k = self.k
        while node:
            right_cnt = node.right.cnt if node.right else 0
            if right_cnt >= k:
                node = node.right
            elif right_cnt + node.freq >= k:
                return node.val
            else:
                k -= right_cnt + node.freq
                node = node.left
                
# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
