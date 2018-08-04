class Solution {
    public List<List<String>> findLadders(String beginWord, String endWord, List<String> wordList) {
        Set<String> dict = new HashSet<>();
        for (String word: wordList)
            dict.add(word);

        List<List<String>> result = new ArrayList<List<String>>();
        if (!dict.contains(endWord))
            return result;
        dict.remove(endWord);

        Queue<String> q = new ArrayDeque<>();
        q.offer(beginWord);

        Map<String, List<String>> parents = new HashMap<String, List<String>>();
        Map<String, Integer> levels = new HashMap<>();
        levels.put(beginWord, 1);
        int level = 0;
        boolean found = false;
        while (!q.isEmpty() && !found) {
            level ++;
            for (int size=q.size(); size > 0; size--) {
                String tmp = q.poll();
                char[] chs = tmp.toCharArray();
                for (int i=0; i < tmp.length(); i++) {
                    char ch = chs[i];
                    for (char c='a'; c <= 'z'; c++) {
                        if (c == ch)
                            continue;
                        chs[i] = c;
                        String temp = new String(chs);
                        if (temp.equals(endWord)) {
                            if (parents.containsKey(endWord)) {
                                parents.get(endWord).add(tmp);
                            } else {
                                List<String> p = new ArrayList<>();
                                p.add(tmp);
                                parents.put(endWord, p);
                            }
                            found = true;
                        } else if (levels.containsKey(temp) && level < levels.get(temp)) {
                            parents.get(temp).add(tmp);
                        }
                        if (!dict.contains(temp))
                            continue;
                        dict.remove(temp);
                        q.offer(temp);
                        levels.put(temp, levels.get(tmp) + 1);
                        List<String> p = new ArrayList<>();
                        p.add(tmp);
                        parents.put(temp, p);
                    }
                    chs[i] = ch;
                }
            }
        }

        if (found) {
            List<String> path = new ArrayList<>();
            path.add(endWord);
            buildPaths(endWord, beginWord, parents, path, result);
        }
        return result;
    }
    private void buildPaths(String word, String beginWord, Map<String, List<String>> parents,
            List<String> path, List<List<String>> result) {
        if (word.equals(beginWord)) {
            List<String> new_path = new ArrayList<>(path);
            Collections.reverse(new_path);
            result.add(new_path);
            return;
        }
        for (String w: parents.get(word)) {
            path.add(w);
            buildPaths(w, beginWord, parents, path, result);
            path.remove(path.size()-1);
        }
    }
}
