import java.util.*;
public class Solution {
    public ArrayList<ArrayList<Integer>> permuteUnique(int[] num) {
        // Start typing your Java solution below
        // DO NOT write main() function
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
}
