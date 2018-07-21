import java.util.*;
public class Solution {
    public List<List<Integer>> permuteUnique(int[] num) {
        Arrays.sort(num);
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        ArrayList<Integer> permutation = new ArrayList<Integer>();
        boolean[] isVisited = new boolean[num.length];
        DFS(result, permutation, num, isVisited);
        return result;
    }
    private void DFS(List<List<Integer>> result, ArrayList<Integer> permutation,
                        int[] num, boolean[] isVisited) {
        if (permutation.size() == num.length) {
            result.add((ArrayList<Integer>)permutation.clone());
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
    public ArrayList<ArrayList<Integer>> permuteUnique(int[] num) {
        ArrayList<ArrayList<Integer>> result = new ArrayList<ArrayList<Integer>>();
        HashSet<ArrayList<Integer>> uniqueResult = new HashSet<ArrayList<Integer>>();
        ArrayList<Integer> temp = new ArrayList<Integer>();
        if (num.length == 1) {
            temp.add(num[0]);
            result.add(temp);
            return result;
        }
        int[] sub = new int[num.length-1];
        for (int i=0; i < sub.length; i++) {
            sub[i] = num[i+1];
        }
        ArrayList<ArrayList<Integer>> v = permuteUnique(sub);
        for (int i=0; i < v.size(); ++i) {
            for (int j=0; j <= v.get(i).size(); j++) {
                temp = (ArrayList<Integer>)v.get(i).clone();
                temp.add(j, num[0]);
                uniqueResult.add(temp);
            }
        }
        for (ArrayList<Integer> a:uniqueResult) {
            result.add(a);
        }
        return result;
    }
    */
}
