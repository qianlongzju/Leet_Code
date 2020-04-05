class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    def __str__(self):
        return " " + str(self.val) + " "

def serialize(root):
    result = []
    current_level = [root]
    next_level = []
    empty = False
    while current_level:
        if empty:
            break
        empty = True
        level_string = []
        for node in current_level:
            if not node:
                level_string.append("None")
                next_level.append(None)
                next_level.append(None)
                continue
            empty = False
            level_string.append(node.val)
            next_level.append(node.left)
            next_level.append(node.right)
        #print len(next_level), empty
        current_level, next_level = next_level, []
        result.append(" ".join([str(s) for s in level_string]))
        #print result
    return "|".join(result)

def deserialize(tree_string):
    if not tree_string: return None
    levels = tree_string.split("|")
    root = TreeNode(int(levels[0]))
    current_level = [root]
    for level in levels[1:]:
        node_vals = level.split(" ")
        node_list = []
        for node_val in node_vals:
            if node_val == 'None':
                node = None
            else:
                node = TreeNode(int(node_val))
            node_list.append(node)
        for i in range(len(current_level)):
            parent = current_level[i]
            if parent is None: continue
            parent.left = node_list[2*i]
            parent.right = node_list[2*i+1]
        current_level = node_list
    return root


a = TreeNode(2)
b = TreeNode(3)
c = TreeNode(4)
d = TreeNode(5)
a.left, a.right = b, c
c.right = d

tree_string = serialize(a)
print tree_string

aa = deserialize(tree_string)
bb, cc = aa.left, aa.right
dd = cc.right
print aa, bb, cc, dd
