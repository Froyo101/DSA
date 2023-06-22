#include <iostream>
#include <string>

using namespace std;

class Solution {
    public:
        static bool isPalindrome(string s) {
            int l = 0, r = s.size() - 1;

            while (l < r) {
                while (!isalnum(s[l]) && l < r) {
                    l++;
                }
                while (!isalnum(s[r]) && l < r) {
                    r--;
                }

                if (tolower(s[l]) != tolower(s[r])) {
                    return false;
                }

                l++;
                r--;
            }

            return true;
        }
};

int main() {
    string s = "babbab";
    bool sol = Solution::isPalindrome(s);
    cout << sol << endl;
    return 0;
}
