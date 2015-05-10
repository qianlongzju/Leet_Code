class Solution:
    # @param {TreeNode} root
    # @return {void} Do not return anything, modify root in-place instead.
    def flatten(self, root):
        cur = root 
        while cur:
            if cur.left:  
                if cur.right:
                    next = cur.left
                    while next.right: next = next.right 
                    next.right = cur.right 
                cur.right = cur.left
                cur.left = None
            cur = cur.right
