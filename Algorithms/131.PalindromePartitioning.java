public class Solution {
    public ArrayList<ArrayList<String>> partition(String s) {
        ArrayList<ArrayList<String>> result = new ArrayList<ArrayList<String>>();
        ArrayList<String> output = new ArrayList<String>();
        DFS(s, 0, output, result);
        return result;
    }
    void DFS(String s, int start, ArrayList<String> output,
        ArrayList<ArrayList<String> > result) {
        if (start == s.length()) {
            result.add((ArrayList<String>)output.clone());
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
