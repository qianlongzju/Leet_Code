/**
 * Definition for binary tree
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    public TreeNode buildTree(int[] inorder, int[] postorder) {
        return buildTreeDriver(inorder, 0, inorder.length-1, postorder, 0, postorder.length-1);
    }
    TreeNode buildTreeDriver(int[] inorder, int inStart, int inEnd, int[] postorder, int postStart, int postEnd) { 	
    	if (postStart > postEnd || inStart > inEnd) {
    		return null;
    	}
    	if (postStart == postEnd) {
    		return new TreeNode(postorder[postStart]);
    	}
    	int rootVal = postorder[postEnd];
    	int rootIndex = 0;
    	for (int i = inStart; i <= inEnd; ++i)
    	{
    		if (inorder[i] == rootVal) {
    			rootIndex = i;
    			break;
    		}
    	}
    	TreeNode root = new TreeNode(rootVal);
    	root.left = buildTreeDriver(inorder, inStart, rootIndex-1, postorder, postStart, postStart+(rootIndex-inStart)-1);
    	root.right = buildTreeDriver(inorder, rootIndex+1, inEnd, postorder, postStart+(rootIndex-inStart), postEnd-1);
    	return root;
    }
}
