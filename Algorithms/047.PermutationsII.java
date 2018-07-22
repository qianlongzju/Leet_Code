public class Solution {
    public List<List<Integer>> permuteUnique(int[] num) {
        Arrays.sort(num);
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        List<Integer> permutation = new ArrayList<>();
        boolean[] isVisited = new boolean[num.length];
        DFS(result, permutation, num, isVisited);
        return result;
    }
    private void DFS(List<List<Integer>> result, List<Integer> permutation,
                        int[] num, boolean[] isVisited) {
        if (permutation.size() == num.length) {
            result.add(new ArrayList<>(permutation));
            return;
        }
        for (int i = 0; i < num.length; i++) {
            if (isVisited[i] == true) continue;
            if (i != 0 && num[i] == num[i-1] && isVisited[i] == isVisited[i-1]) continue;
            isVisited[i] = true;
            permutation.add(num[i]);
            DFS(result, permutation, num, isVisited);
            permutation.remove(permutation.size()-1);
            isVisited[i] = false;
        }
    }
    /*
    public List<List<Integer>> permuteUnique(int[] num) {
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        Set<List<Integer>> uniqueResult = new HashSet<List<Integer>>();
        List<Integer> temp = new ArrayList<>();
        if (num.length == 1) {
            temp.add(num[0]);
            result.add(temp);
            return result;
        }
        int[] sub = new int[num.length-1];
        for (int i=0; i < sub.length; i++) {
            sub[i] = num[i+1];
        }
        List<List<Integer>> v = permuteUnique(sub);
        for (int i=0; i < v.size(); ++i) {
            for (int j=0; j <= v.get(i).size(); j++) {
                temp = new ArrayList<>(v.get(i));
                temp.add(j, num[0]);
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
