class Solution {
public:
    bool isPalindrome(string s) {
      for (char& c: s) {
        int isUpper = isupper(c);
        if (isUpper != 0) {
          c = tolower(c);
        }
      }
      
      int l = 0;
      int r = s.size() - 1;

      std::cout << s;
      while (l < r) {
        int lIsAlnum = isalnum(s[l]);
        int rIsAlnum = isalnum(s[r]);

        if (s[l] == s[r]) {
          l++;
          r--;
        }
        else if (s[l] == ' ') l++;
        else if (s[r] == ' ') r--;
        else if (lIsAlnum == 0) l++;
        else if (rIsAlnum == 0) r--;
        else {return false;}
      }
       return true; 
    }
};
