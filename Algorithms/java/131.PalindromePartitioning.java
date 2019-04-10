public class Solution {
    public List<List<String>> partition(String s) {
        List<List<String>> result = new ArrayList<List<String>>();
        List<String> output = new ArrayList<>();
        DFS(s, 0, output, result);
        return result;
    }
    void DFS(String s, int start, List<String> output,
        List<List<String>> result) {
        if (start == s.length()) {
            result.add(new ArrayList<>(output));
            return;
        }
        for (int i = start; i < s.length(); i++) {
            if (isPalindrome(s, start, i)) {
                output.add(s.substring(start, i+1));
                DFS(s, i + 1, output, result);
                output.remove(output.size()-1);
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
