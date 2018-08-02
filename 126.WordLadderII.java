public class Solution {
    public List<List<String>> findLadders(String start, String end, Set<String> dict) {
        List<List<String>> result = new ArrayList<List<String>>();
        List<String> q = new LinkedList<>();
        q.add(start);
        Set<String> visited = new HashSet<>();
        visited.add(start);
        Map<String, List<String>> m = new HashMap<>();
        Map<String, Integer> level = new HashMap<>();
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
                            m.put(end, new ArrayList<>());
                        }
                        m.get(end).add(tmp);
                    } else if (dict.contains(temp)) {
                        if (!visited.contains(temp)) {
                            q.add(temp);
                            visited.add(temp);
                            m.put(temp,  new ArrayList<>());
                            m.get(temp).add(tmp);
                            level.put(temp,  level.get(tmp) + 1);
                        } else if (level.get(tmp)+1 == level.get(temp)) {
                            m.get(temp).add(tmp);
                        }
                    }
                }
            }
        }
        List<String> path = new ArrayList<>();
        buildPaths(start, end, m, path, result);
        return result;
    }
    void buildPaths(String start, String end, Map<String, List<String>> m, 
            List<String> path, List<List<String>> result) {
        if (end.equals(start)) {
            List<String> clone = new ArrayList<>(path);
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
