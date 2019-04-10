public class Solution {
    public List<String> fullJustify(String[] words, int maxWidth) {
        List<String> result = new ArrayList<>();
        int start = 0;
        int length = 0;
        int count = 0;
        String s = "";
        String space = " ";
        int i;
        for (i=0; i < words.length; ++i) {
            if (length + count + words[i].length() > maxWidth) {
                if (count == 1) {
                    s = words[start];
                    while (s.length() < maxWidth) {
                        s += space;
                    }
                } else {
                    int numSpace = maxWidth - length;
                    s = "";
                    for (int j=start; j < i-1; j++) {
                        s += words[j];
                        for (int k=0; k < (numSpace/(count-1)); k++) {
                            s += space;
                        }
                        if (numSpace%(count-1) != 0) {
                            s += space;
                            numSpace --;
                        }
                    }
                    s += words[i-1];
                }
                result.add(s);
                length = words[i].length();
                start = i;
                count = 1;
            } else {
                count ++;
                length += words[i].length();
            }
        } 
        s = words[start];
        for (int j=start+1; j < words.length; j++) {
            s += space + words[j];
        }
        while (s.length() < maxWidth) {
            s += space;
        }
        result.add(s);
        return result;
    }
}
