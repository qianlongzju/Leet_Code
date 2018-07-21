public class Solution {
    public String minWindow(String S, String T) {
        // Note: The Solution object is instantiated only once and is reused by each test case.
        int[] needToFind = new int[256];
        int[] hasFound = new int[256];
        for (int i=0; i < 256; ++i) {
            needToFind[i] = 0;
            hasFound[i] = 0;
        }
        for (int i=0; i < T.length(); ++i) {
            needToFind[T.charAt(i)] ++;
        }
        int count = 0;
        int begin = 0;
        int end = 0;
        int minLength = Integer.MAX_VALUE;
        int startIndex = 0;
        while (end < S.length()) {
            if (needToFind[S.charAt(end)] == 0) {
                end ++;
                continue;
            }
            hasFound[S.charAt(end)] ++;
            if (hasFound[S.charAt(end)] <= needToFind[S.charAt(end)]) {
                count ++;
            }
            if (count == T.length()) {
                while (needToFind[S.charAt(begin)] == 0 || hasFound[S.charAt(begin)] > needToFind[S.charAt(begin)]) {
                    if (hasFound[S.charAt(begin)] > needToFind[S.charAt(begin)]) {
                        hasFound[S.charAt(begin)] --;
                    }
                    begin ++;
                }
                int length = end - begin + 1;
                if (length < minLength) {
                    minLength = length;
                    startIndex = begin;
                }
            }
            end ++;
        }
        if (count == T.length()) {
            return S.substring(startIndex, startIndex + minLength);
        } else {
            return "";
        }
    }
}
