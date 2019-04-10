class Solution {
public:
    vector<int> findAnagrams(string s, string p) {
        vector<int> result;
        int m = s.length();
        int n = p.length();
        if (m < n) {
            return result;
        }
        for (int i=0; i <= m-n; i++) {
            int num[26];
            for (int j=0; j < 26; j++) {
                num[j] = 0;
            }
            for (int j=0; j < n; j++) {
                num[s[i+j]-'a'] ++;
                num[p[j]-'a'] --;
            }
            bool flag = true;
            for (int j=0; j < 26; j++) {
                if (num[j] != 0) {
                    flag = false;
                    break;
                }
            }
            if (flag) {
                result.push_back(i);
            }
        }
        return result;
    }
};
/*
 * class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        result = []
        if len(s) < len(p):
            return result
        m, n = len(s), len(p)
        for i in range(m-n+1):
            nums = [0] * 26
            for j in range(n):
                nums[ord(s[i+j]) - ord('a')] += 1
                nums[ord(p[j]) - ord('a')] -= 1
            for j in range(len(nums)):
                if nums[j] != 0:
                    break
            else:
                result.append(i)
        return result
*/

