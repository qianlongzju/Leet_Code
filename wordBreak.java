import java.util.*;
public class Solution {
    public boolean wordBreak(String s, Set<String> dict) {
        // Note: The Solution object is instantiated only once and is reused by each test case.
        int n = s.length();
        boolean[] wb = new boolean[n];
        for (int i=0; i < n; i++) {
           wb[i] = false; 
        }
        for (int i=0; i < n; ++i) {
            if (wb[i] == false && dict.contains(s.substring(0, i+1))) {
                wb[i] = true;
            }
            if (wb[i] == true) {
                if (i == n-1) {
                    return true;
                }
                for (int j=i+1; j < n; ++j) {
                    if (wb[j] == false && dict.contains(s.substring(i+1, j+1))) {
                        wb[j] = true;
                    }
                    if (j == n-1 && wb[j] == true) {
                        return true;
                    }
                }
            }
        }
        return false;
    }
}
