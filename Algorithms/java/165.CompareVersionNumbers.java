public class Solution {
    public int compareVersion(String version1, String version2) {
        String[] tokens1 = version1.split("\\.");
        String[] tokens2 = version2.split("\\.");
        int length = Integer.max(tokens1.length, tokens2.length);
        for (int i = 0; i < length; i++) {
            int a = 0, b=0;
            if (i < tokens1.length)
                a = Integer.parseInt(tokens1[i]);
            if (i < tokens2.length)
                b = Integer.parseInt(tokens2[i]);
            if (a > b)
                return 1;
            if (a < b)
                return -1;
        }
        return 0;
    }
}
