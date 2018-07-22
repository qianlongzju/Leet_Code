public class Solution {
    public List<List<Integer>> permute(int[] num) {
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
            isVisited[i] = true;
            permutation.add(num[i]);
            DFS(result, permutation, num, isVisited);
            permutation.remove(permutation.size()-1);
            isVisited[i] = false;
        }
    }
    /*
    public List<List<Integer>> permute(int[] num) {
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        permute(num, 0, result);
        return result;
    }
    public void permute(int[] num, int index, List<List<Integer>> result) {
        if (num.length == index) {
            List<Integer> temp = new ArrayList<>();
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
    public List<List<Integer>> permute(int[] num) {
        List<List<Integer>> result = new ArrayList<List<Integer>>();
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
        List<List<Integer>> v = permute(sub);
        for (int i=0; i < v.size(); ++i) {
            for (int j=0; j < v.get(i).size(); j++) {
                temp = new ArrayList<>(v.get(i));
                int tmp = temp.get(j);
                temp.set(j, num[0]);
                temp.add(0, tmp);
                result.add(temp);
            }
            temp = new ArrayList<>(v.get(i));
            temp.add(0, num[0]);
            result.add(temp);
        }
        return result;
    }
    public List<List<Integer>> permute(int[] num) {
        List<List<Integer>> result = new ArrayList<List<Integer>>();
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
        List<List<Integer>> v = permute(sub);
        for (int i=0; i < v.size(); ++i) {
            for (int j=0; j <= v.get(i).size(); j++) {
                temp = new ArrayList<>(v.get(i));
                temp.add(j, num[0]);
                result.add(temp);
            }
        }
        return result;
    }
    */
}
