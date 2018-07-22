public class Solution {
    public TreeNode sortedArrayToBST(int[] nums) {
        return sortedArrayToBST(nums, 0, nums.length-1);
    }
    private TreeNode sortedArrayToBST(int[] nums, int start, int end) {
        if (start > end) return null;
        int middle = start + (end-start)/2;
        TreeNode root = new TreeNode(nums[middle]);
        root.left = sortedArrayToBST(nums, start, middle-1);
        root.right = sortedArrayToBST(nums, middle+1, end);
        return root;
    }
}
