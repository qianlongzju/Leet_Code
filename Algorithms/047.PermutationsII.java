public class Solution {
    public List<List<Integer>> permuteUnique(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        List<Integer> permutation = new ArrayList<>();
        boolean[] isVisited = new boolean[nums.length];
        DFS(result, permutation, nums, isVisited);
        return result;
    }
    private void DFS(List<List<Integer>> result, List<Integer> permutation,
                        int[] nums, boolean[] isVisited) {
        if (permutation.size() == nums.length) {
            result.add(new ArrayList<>(permutation));
            return;
        }
        for (int i = 0; i < nums.length; i++) {
            if (isVisited[i] == true) continue;
            if (i != 0 && nums[i] == nums[i-1] && isVisited[i] == isVisited[i-1]) continue;
            isVisited[i] = true;
            permutation.add(nums[i]);
            DFS(result, permutation, nums, isVisited);
            permutation.remove(permutation.size()-1);
            isVisited[i] = false;
        }
    }
    /*
    public List<List<Integer>> permuteUnique(int[] nums) {
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        Set<List<Integer>> uniqueResult = new HashSet<List<Integer>>();
        List<Integer> temp = new ArrayList<>();
        if (nums.length == 1) {
            temp.add(nums[0]);
            result.add(temp);
            return result;
        }
        int[] sub = new int[nums.length-1];
        for (int i=0; i < sub.length; i++) {
            sub[i] = nums[i+1];
        }
        List<List<Integer>> v = permuteUnique(sub);
        for (int i=0; i < v.size(); ++i) {
            for (int j=0; j <= v.get(i).size(); j++) {
                temp = new ArrayList<>(v.get(i));
                temp.add(j, nums[0]);
                uniqueResult.add(temp);
            }
        }
        for (List<Integer> a:uniqueResult) {
            result.add(a);
        }
        return result;
    }
    */
}
