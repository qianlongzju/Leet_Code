public class Solution {
    public List<List<Integer>> fourSum(int[] nums, int target) {
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        Set<List<Integer>> quadplets = new HashSet<List<Integer>>();
        List<Integer> quadplet = new ArrayList<>();
        Arrays.sort(nums);
        int n = nums.length;
        for (int i = 0; i < n; i++) {
            for (int j = i+1; j < n; j++) {
                int k = j + 1;
                int l = n - 1;
                while (k < l) {
                    int sum_four = nums[i] + nums[j] + nums[k] + nums[l];
                    if (sum_four < target) {
                        k++;
                    } else if (sum_four > target) {
                        l--;
                    } else {
                        quadplet.add(nums[i]);
                        quadplet.add(nums[j]);
                        quadplet.add(nums[k]);
                        quadplet.add(nums[l]);
                        quadplets.add(quadplet);
                        quadplet = new ArrayList<Integer>();
                        k++;
                        l--;
                    }
                }
            }
        }
        for (List<Integer> a:quadplets)
            result.add(a);
        return result;
    }
}
