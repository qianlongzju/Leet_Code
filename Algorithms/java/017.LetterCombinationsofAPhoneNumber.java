public class Solution {
    public List<String> letterCombinations(String digits) {
        String[] digitStrings = {"", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
        List<String> result = new ArrayList<>();
        String phone = "";
        DFS(result, phone, digits, digitStrings, 0);
        return result;
    }
    private void DFS(List<String> result, String phone, String digits, 
                        String[] digitStrings, int level) {
        if (level == digits.length()) {
            if (level != 0) result.add(phone);
            return;
        }
        String temp = digitStrings[digits.charAt(level) - '0'];
        for (int i = 0; i < temp.length(); i++) {
            phone += temp.charAt(i);
            DFS(result, phone, digits, digitStrings, level+1);
            phone = phone.substring(0, phone.length()-1);
        }
    }
    /*
    public List<String> letterCombinations(String digits) {
        String[] digitStrings = {"abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
        List<String> letters = new ArrayList<>();
        letters.add("");
        for (int i=0; i < digits.length(); i++){
            while (true){
                String s = letters.get(0);
                if (s.length() > i) break;
                letters.remove(0);
                for (char d: digitStrings[digits.charAt(i)-'0'-2].toCharArray()) {
                    letters.add(s+d);
                }
            }
        }
        return letters;
    }
    */
}
