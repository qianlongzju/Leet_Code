public class Solution {
    public List<List<Integer>> permute(int[] nums) {
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
            isVisited[i] = true;
            permutation.add(nums[i]);
            DFS(result, permutation, nums, isVisited);
            permutation.remove(permutation.size()-1);
            isVisited[i] = false;
        }
    }
    /*
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        permute(nums, 0, result);
        return result;
    }
    public void permute(int[] nums, int index, List<List<Integer>> result) {
        if (nums.length == index) {
            List<Integer> temp = new ArrayList<>();
            for (int i = 0; i < nums.length; i++) {
                temp.add(nums[i]);
            }
            result.add(temp);
            return;
        }
        for (int i=index; i < nums.length; ++i) {
            int tmp = nums[i];
            nums[i] = nums[index];
            nums[index] = tmp;
            permute(nums, index+1, result);
            tmp = nums[i];
            nums[i] = nums[index];
            nums[index] = tmp;
        }
    }
    */
    /*
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> result = new ArrayList<List<Integer>>();
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
        List<List<Integer>> v = permute(sub);
        for (int i=0; i < v.size(); ++i) {
            for (int j=0; j < v.get(i).size(); j++) {
                temp = new ArrayList<>(v.get(i));
                int tmp = temp.get(j);
                temp.set(j, nums[0]);
                temp.add(0, tmp);
                result.add(temp);
            }
            temp = new ArrayList<>(v.get(i));
            temp.add(0, nums[0]);
            result.add(temp);
        }
        return result;
    }
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> result = new ArrayList<List<Integer>>();
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
        List<List<Integer>> v = permute(sub);
        for (int i=0; i < v.size(); ++i) {
            for (int j=0; j <= v.get(i).size(); j++) {
                temp = new ArrayList<>(v.get(i));
                temp.add(j, nums[0]);
                result.add(temp);
            }
        }
        return result;
    }
    */
}
