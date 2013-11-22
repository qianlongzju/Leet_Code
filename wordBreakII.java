import java.util.*;
public class Solution {
    public ArrayList<String> wordBreak(String s, Set<String> dict) {
        // Note: The Solution object is instantiated only once and is reused by each test case.
        // 长度为 n 的字符串有 n+1 个隔板
        int n = s.length();
        boolean[] f = new boolean[n+1];
        f[0] = true;
        for (int i=1; i <= n; i++)
            f[i] = false;
        // path[i][j] 为 true,表示 s[j, i) 是一个合法单词,可以从 j 处切开
        // 第一行未用
        boolean[][] prev = new boolean[n+1][n];
        for (int i=0; i <= n; i++)
            for (int j=0; j < n; j++)
                prev[i][j] = false;
        for (int i = 1; i <= n; ++i) {
            for (int j = i - 1; j >= 0; --j) {
                if (f[j] && dict.contains(s.substring(j, i))) {
                    f[i] = true;
                    prev[i][j] = true;
                }
            }
        }
        ArrayList<String> result = new ArrayList<String>();
        ArrayList<String> path = new ArrayList<String>();
        gen_path(s, prev, n, path, result);
        return result;
    }
    // DFS 遍历树,生成路径
    private void gen_path(String s, boolean[][] prev,
            int cur, ArrayList<String> path, ArrayList<String> result) {
        if (cur == 0) {
            String tmp = "";
            for (int i=path.size()-1; i >= 0; i--) {
                tmp += path.get(i);
                if (i != 0)
                    tmp += " ";
            }
            result.add(tmp);
        }
        for (int i = 0; i < cur; ++i) {
            if (prev[cur][i]) {
                path.add(s.substring(i, cur));
                gen_path(s, prev, i, path, result);
                path.remove(path.size()-1);
            }
        }
    }
}
