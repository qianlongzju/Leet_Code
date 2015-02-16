public class Solution {
    public ArrayList<String> letterCombinations(String digits) {
        String[] digitStrings = {"abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
        ArrayList<String> letters = new ArrayList<String>();
        letters.add("");
        for (int i=0; i < digits.length(); i++){
            while (true){
                String s = letters.get(0);
                if (s.length() > i){
                    break;
                }
                letters.remove(0);
                for (char d: digitStrings[digits.charAt(i)-'0'-2].toCharArray()) {
                    letters.add(s+d);
                }
            }
        }
        return letters;
    }
}
