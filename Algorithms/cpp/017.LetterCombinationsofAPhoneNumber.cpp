class Solution {
public:
    vector<string> letterCombinations(string digits) {
        string digitStrings[] = {"", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
        vector<string> result;
        string phone;
        DFS(result, phone, digits, digitStrings, 0);
        return result;
    }
    void DFS(vector<string>& result, string phone, string digits, string digitStrings[], int level) {
        if (level == digits.size()) {
            if (level != 0) result.push_back(phone);
            return;
        }
        string temp = digitStrings[digits[level]-'0'];
        for (int i = 0; i < temp.size(); i++) {
            phone += temp[i];
            DFS(result, phone, digits, digitStrings, level+1);
            phone.pop_back(); 
        }
    }
    /*
    vector<string> letterCombinations(string digits) {
        string digitStrings[] = {"abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
        vector<string> letters;
        letters.push_back("");
        for (int i=0; i < digits.size(); i++){
            string digitString = digitStrings[digits[i]-'0'-2];
            while (true){
                string s = letters[0];
                if (s.size() > i) break;
                letters.erase(letters.begin());
                for (int j=0; j < digitString.size(); j++) {
                    letters.push_back(s + digitString[j]);
                }
            }
        }
        return letters;
    }
    */
};
