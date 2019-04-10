class Solution:
    # @param {integer} n
    # @return {TreeNode[]}
    def generateTrees(self, n):
        result = self.generateTreesHelper(1, n)
        if len(result) == 1 and result[0] == None:
            return []
        return result

    def generateTreesHelper(self, start, end):
        result = []
        if start > end:
            result.append(None)
            return result
        if start == end:
            root = TreeNode(start)
            result.append(root)
            return result
        for i in range(start, end+1):
            left = self.generateTreesHelper(start, i-1)
            right = self.generateTreesHelper(i+1, end)
            for j in range(len(left)):
                for k in range(len(right)):
                    root = TreeNode(i)
                    root.left = left[j]
                    root.right = right[k]
                    result.append(root)
        return result
