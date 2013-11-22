import java.util.*;
public class Solution {
    public ArrayList<ArrayList<String>> partition(String s) {
        // Start typing your Java solution below
        // DO NOT write main() function
        ArrayList<ArrayList<String>> result = new ArrayList<ArrayList<String>>();
        ArrayList<String> output = new ArrayList<String>(); // 一个 partition 方案
        DFS(s, 0, output, result);
        return result;
    }
    // 搜索必须以 s[start] 开头的 partition 方案
    void DFS(String s, int start, ArrayList<String> output,
        ArrayList<ArrayList<String> > result) {
        if (start == s.length()) {
            result.add((ArrayList<String>)output.clone());
            return;
        }
        for (int i = start; i < s.length(); i++) {
            if (isPalindrome(s, start, i)) { // 从 i 位置砍一刀
                output.add(s.substring(start, i+1));
                DFS(s, i + 1, output, result); // 继续往下砍
                output.remove(output.size()-1); // 撤销上一个 push_back 的砍
            }
        }
    }
    boolean isPalindrome(String s, int start, int end) {
        while (start < end) {
            if (s.charAt(start) != s.charAt(end)) return false;
            start++;
            end--;
        }
        return true;
    }
}
