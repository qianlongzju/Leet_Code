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
    public TreeNode sortedArrayToBST(int[] num) {
        return sortedArrayToBST(num, 0, num.length-1);
    }
    private TreeNode sortedArrayToBST(int[] num, int start, int end) {
        if (start > end) return null;
        int middle = start + (end-start)/2;
        TreeNode root = new TreeNode(num[middle]);
        root.left = sortedArrayToBST(num, start, middle-1);
        root.right = sortedArrayToBST(num, middle+1, end);
        return root;
    }
}
