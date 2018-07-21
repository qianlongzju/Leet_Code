class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        Set<List<Integer>> triplets = new HashSet<List<Integer>>();
        List<Integer> triplet = new ArrayList<Integer>();
        Arrays.sort(nums);
        int n = nums.length;
        for (int i = 0; i < n; i++) {
            while (i > 0 && i < n && nums[i] == nums[i-1])
                i++;
            int j = i + 1;
            int k = n - 1;
            while (j < k) {
                int total = nums[i] + nums[j] + nums[k];
                if (total < 0) {
                    j++;
                    while (j < k && nums[j] == nums[j-1])
                        j++;
                } else if (total > 0) {
                    k--;
                    while (k > j && nums[k] == nums[k+1])
                        k--;
                } else {
                    triplet.add(nums[i]);
                    triplet.add(nums[j]);
                    triplet.add(nums[k]);
                    triplets.add(triplet);
                    triplet = new ArrayList<Integer>();
                    j++;
                    while (j < k && nums[j] == nums[j-1])
                        j++;
                    k--;
                    while (k > j && nums[k] == nums[k+1])
                        k--;
                }
            }
        }
        for (List<Integer> a:triplets)
            result.add(a);
        return result;
    }
}
