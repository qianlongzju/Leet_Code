import java.util.*;
public class Solution {
    public ArrayList<String> anagrams(String[] strs) {
        ArrayList<String> result = new ArrayList<String>();
        HashMap<String, ArrayList<String>> m = new HashMap<String, ArrayList<String>>();
        for (int i=0; i < strs.length; ++i) {
            char[] chars = strs[i].toCharArray();
            Arrays.sort(chars);
            String temp = new String(chars);
            if (m.get(temp) == null) {
                ArrayList<String> a = new ArrayList<String>();
                a.add(strs[i]);
                m.put(temp, a);
            } else {
                m.get(temp).add(strs[i]);
            }
        }
        for (ArrayList<String> it: m.values()) {
            if (it.size() > 1) {
                result.addAll(it);
            }
        }
        return result;
    }
}
