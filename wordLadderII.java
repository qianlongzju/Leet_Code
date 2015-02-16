import java.util.*;
public class Solution {
    public ArrayList<ArrayList<String>> findLadders(String start, String end, HashSet<String> dict) {
        ArrayList<ArrayList<String>> result = new ArrayList<ArrayList<String>>();
        LinkedList<String> q = new LinkedList<String>();
        q.add(start);
        HashSet<String> visited = new HashSet<String>();
        visited.add(start);
        HashMap<String, ArrayList<String>> m = new HashMap<String, ArrayList<String>>();
        HashMap<String, Integer> level = new HashMap<String, Integer>();
        level.put(start, 1);
        int maxLevel = -1;
        while (!q.isEmpty()) {
            String tmp = q.remove();
            if (maxLevel != -1 && level.get(tmp) > maxLevel) {
                break;
            }
            for (int i=0; i < tmp.length(); i++) {
                for (char c='a'; c <= 'z'; c++) {
                    if (c == tmp.charAt(i)) {
                        continue;
                    }
                    char[] chars = tmp.toCharArray();
                    chars[i] = c;
                    String temp = new String(chars);
                    if (temp.equals(end)) {
                        maxLevel = level.get(tmp);
                        if (!m.containsKey(end)) {
                            m.put(end, new ArrayList<String>());
                        }
                        m.get(end).add(tmp);
                    } else if (dict.contains(temp)) {
                        if (!visited.contains(temp)) {
                            q.add(temp);
                            visited.add(temp);
                            m.put(temp,  new ArrayList<String>());
                            m.get(temp).add(tmp);
                            level.put(temp,  level.get(tmp) + 1);
                        } else if (level.get(tmp)+1 == level.get(temp)) {
                            m.get(temp).add(tmp);
                        }
                    }
                }
            }
        }
        ArrayList<String> path = new ArrayList<String>();
        buildPaths(start, end, m, path, result);
        return result;
    }
    void buildPaths(String start, String end, HashMap<String, ArrayList<String>> m, 
            ArrayList<String> path, ArrayList<ArrayList<String>> result) {
        if (end.equals(start)) {
            ArrayList<String> clone = (ArrayList<String>)path.clone();
            clone.add(0, start);
            result.add(clone);
            return;
        }
        path.add(0, end);
        for (int i=0; m.containsKey(end) && i < m.get(end).size(); ++i) {
            buildPaths(start, m.get(end).get(i), m, path, result);
        }
        path.remove(0);
    }
}
