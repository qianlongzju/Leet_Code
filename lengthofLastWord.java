public class Solution {
    public int lengthOfLastWord(String s) {
        int n = s.length();
        if (n == 0) {
            return 0;
        }
        boolean wordBegin = false;
        int count = 0;
        for (int i=n-1; i >= 0; i--) {
            if (s.charAt(i) != ' ') {
                if (wordBegin) {
                    count++;
                }
                else {
                    wordBegin = true;
                    count++;
                }
            }
            else {
                if (wordBegin) {
                    return count;
                }
            }
        }
        return count;
    }
}
