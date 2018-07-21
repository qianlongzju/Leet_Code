import java.util.*;
public class Solution {
    public List<List<Integer>> permute(int[] num) {
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
            isVisited[i] = true;
            permutation.add(num[i]);
            DFS(result, permutation, num, isVisited);
            permutation.remove(permutation.size()-1);
            isVisited[i] = false;
        }
    }
    /*
    public ArrayList<ArrayList<Integer>> permute(int[] num) {
        ArrayList<ArrayList<Integer>> result = new ArrayList<ArrayList<Integer>>();
        permute(num, 0, result);
        return result;
    }
    public void permute(int[] num, int index, ArrayList<ArrayList<Integer>> result) {
        if (num.length == index) {
            ArrayList<Integer> temp = new ArrayList<Integer>();
            for (int i = 0; i < num.length; i++) {
                temp.add(num[i]);
            }
            result.add(temp);
            return;
        }
        for (int i=index; i < num.length; ++i) {
            int tmp = num[i];
            num[i] = num[index];
            num[index] = tmp;
            permute(num, index+1, result);
            tmp = num[i];
            num[i] = num[index];
            num[index] = tmp;
        }
    }
    */
    /*
    public ArrayList<ArrayList<Integer>> permute(int[] num) {
        ArrayList<ArrayList<Integer>> result = new ArrayList<ArrayList<Integer>>();
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
        ArrayList<ArrayList<Integer>> v = permute(sub);
        for (int i=0; i < v.size(); ++i) {
            for (int j=0; j < v.get(i).size(); j++) {
                temp = (ArrayList<Integer>)v.get(i).clone();
                int tmp = temp.get(j);
                temp.set(j, num[0]);
                temp.add(0, tmp);
                result.add(temp);
            }
            temp = (ArrayList<Integer>)v.get(i).clone();
            temp.add(0, num[0]);
            result.add(temp);
        }
        return result;
    }
    public ArrayList<ArrayList<Integer>> permute(int[] num) {
        ArrayList<ArrayList<Integer>> result = new ArrayList<ArrayList<Integer>>();
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
        ArrayList<ArrayList<Integer>> v = permute(sub);
        for (int i=0; i < v.size(); ++i) {
            for (int j=0; j <= v.get(i).size(); j++) {
                temp = (ArrayList<Integer>)v.get(i).clone();
                temp.add(j, num[0]);
                result.add(temp);
            }
        }
        return result;
    }
    */
}