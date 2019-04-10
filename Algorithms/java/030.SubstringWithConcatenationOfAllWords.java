public class Solution {
    public List<Integer> findSubstring(String s, String[] words) {
        List<Integer> result = new ArrayList<>();
        if (words.length == 0)
            return result;
        int wordLength = words[0].length();
        int subLength = wordLength * words.length;
        int length = s.length();
        Map<String, Integer>  wordCount = new HashMap<>();
        Map<String, Integer>  current = new HashMap<>();
        for (int i=0; i < words.length; ++i) {
            if (wordCount.containsKey(words[i]))
                wordCount.put(words[i], wordCount.get(words[i])+1);
            else
                wordCount.put(words[i], 1);
        }
        for (int i=0; i <= length-subLength; i++) {
            current.clear();
            int j;
            for (j=0; j < words.length; j++) {
                String word = s.substring(i + j*wordLength, i + (j+1)*wordLength);
                if (!wordCount.containsKey(word))
                    break;
                if (current.containsKey(word))
                    current.put(word, current.get(word)+1);
                else
                    current.put(word, 1);
                if (current.get(word) > wordCount.get(word))
                    break;
            }
            if (j == words.length)
                result.add(i);
        }
        return result;
    }
}
