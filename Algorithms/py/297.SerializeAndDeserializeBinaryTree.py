# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        #if root == None:
        #    return "#,"
        #return str(root.val) + "," + self.serialize(root.left) + self.serialize(root.right)
        q = [root]
        result = []
        while q:
            node = q.pop(0)
            if node == None:
                result.append('#')
            else:
                result.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
        return ",".join(result)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        vals = data.strip(",").split(",")
        if vals[0] == '#':
            return None
        root = TreeNode(str(vals[0]))
        q = [root]
        i = 1
        while i < len(vals):
            cur = q.pop(0)
            if vals[i] != '#':
                cur.left = TreeNode(int(vals[i]))
                q.append(cur.left)
            i += 1
            if vals[i] != '#':
                cur.right = TreeNode(int(vals[i]))
                q.append(cur.right)
            i += 1
        return root

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        def rserialize(root, string):
            """ a recursive helper function for the serialize() function."""
            # check base case
            if root is None:
                string += 'None,'
            else:
                string += str(root.val) + ','
                string = rserialize(root.left, string)
                string = rserialize(root.right, string)
            return string

        return rserialize(root, '')

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        def rdeserialize(l):
            """ a recursive helper function for deserialization."""
            if l[0] == 'None':
                l.pop(0)
                return None

            root = TreeNode(l[0])
            l.pop(0)
            root.left = rdeserialize(l)
            root.right = rdeserialize(l)
            return root

        data_list = data.split(',')
        root = rdeserialize(data_list)
        return root
def print_q(q):
    for node in q:
        print(node.val, end=' ')
    print()

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
codec = Codec()
nodes = [TreeNode(i) for i in range(1, 6)]
nodes[0].left, nodes[0].right = nodes[1], nodes[2]
nodes[2].left, nodes[2].right = nodes[3], nodes[4]
root = nodes[0]
print(codec.serialize(root))
print(codec.deserialize(codec.serialize(root)))
