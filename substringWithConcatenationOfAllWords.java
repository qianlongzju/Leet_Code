import java.util.*;
public class Solution {
    public ArrayList<Integer> findSubstring(String S, String[] L) {
        ArrayList<Integer> result = new ArrayList<Integer>();
        int wordLength = L[0].length();
        int subLength = wordLength * L.length;
        int length = S.length();
        HashMap<String, Integer>  wordCount = new HashMap<String, Integer>();
        HashMap<String, Integer>  current = new HashMap<String, Integer>();
        for (int i=0; i < L.length; ++i) {
            if (wordCount.containsKey(L[i]))
                wordCount.put(L[i], wordCount.get(L[i])+1);
            else 
                wordCount.put(L[i], 1);
        }
        for (int i=0; i <= length-subLength; i++) {
            current.clear();
            int j;
            for (j=0; j < L.length; j++) {
                String word = S.substring(i + j*wordLength, i + (j+1)*wordLength);
                if (!wordCount.containsKey(word))
                    break;
                if (current.containsKey(word))
                    current.put(word, current.get(word)+1);
                else
                    current.put(word, 1);
                if (current.get(word) > wordCount.get(word))
                    break;
            }
            if (j == L.length)
                result.add(i);
        }
        return result;
    }
}
