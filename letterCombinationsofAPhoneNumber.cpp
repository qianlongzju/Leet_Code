#include "leetcode.h"
class Solution {
public:
    vector<string> letterCombinations(string digits) {
        string digitStrings[] = {"abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
        vector<string> letters;
        letters.push_back("");
        for (int i=0; i < digits.size(); i++){
            string digitString = digitStrings[digits[i]-'0'-2];
            while (true){
                string s = letters[0];
                if (s.size() > i){
                    break;
                }
                letters.erase(letters.begin());
                for (int j=0; j < digitString.size(); j++) {
                    letters.push_back(s + digitString[j]);
                }
            }
        }
        return letters;
    }
};
