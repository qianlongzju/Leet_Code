class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int n = s.length(), i = 0, j = 0, maxLen = 0;
        bool exist[256] = { false };
        while (j < n) {
            if (exist[s[j]]) {
                maxLen = max(maxLen, j-i);
                while (s[i] != s[j]) {
                    exist[s[i]] = false;
                    i++;
                }
                i++;
            } else {
                exist[s[j]] = true;
            }
            j++;
        }
        return max(maxLen, n-i);
    }
};
int main(int argc, char const *argv[])
{
    Solution s;
    cout << s.lengthOfLongestSubstring("wlrbbmqbhcdarzowkkyhiddqscdxrjmowfrxsjybldbefsarcbynecdyggxxpklorellnmpapqfwkhopkmco"
) << endl;
    return 0;
}
