class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root: return
        old_root = root
        while root:
            curr_node = root
            while curr_node:
                if curr_node.left:
                    curr_node.left.next = curr_node.right
                if curr_node.right:
                    curr_node.right.next = curr_node.next.left if curr_node.next else None
                curr_node = curr_node.next
            root = root.left
        return old_root

    # not constant extra space
    #def connect(self, root):
    #    if not root: return
    #    q, next_level_q, previous= [root], [], None
    #    while q:
    #        p = q.pop(0)
    #        if previous:
    #            previous.next = p
    #        previous = p
    #        if p.left:
    #            next_level_q.append(p.left)
    #        if p.right:
    #            next_level_q.append(p.right)
    #        if not q:
    #            p.next = None
    #            q, next_level_q = next_level_q, []
    #            previous = None
