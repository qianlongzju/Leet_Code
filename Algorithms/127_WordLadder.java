public class Solution {
      public int ladderLength(String start, String end, Set<String> wordDict) {
        if (start.equals(end)) {
            return 2;
        }
        LinkedList<String> q = new LinkedList<String>();
        q.push(start);
        Set<String> visited = new HashSet<String>();
        visited.add(start);
        Map<String, String> m = new HashMap<String, String>();
        while (!q.isEmpty()) {
            String tmp = q.remove();
            for (int i=0; i < tmp.length(); i++) {
                for (char c='a'; c <= 'z'; c++) {
                    if (c == tmp.charAt(i)) continue;
                    char[] t = tmp.toCharArray();
                    t[i] = c;
                    String temp = new String(t);
                    if (temp.equals(end)) {
                        int length = 2;
                        while (!tmp.equals(start)) {
                            tmp = m.get(tmp);
                            length ++;
                        }
                        return length;
                    }
                    if (wordDict.contains(temp) &&
                            !visited.contains(temp)) {
                        q.add(temp);
                        visited.add(temp);
                        m.put(temp, tmp);
                    }
                }
            }
        }
        return 0;
    }
}
