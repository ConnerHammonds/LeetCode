class Solution {
public:
    string reverseWords(string s) {
      string res = "";
      int l = s.size() - 1;
      int r = s.size() - 1;

      while (l >= 0) {

        while (l >= 0 && s[l] != ' ') {
          l--;  
        }

        res += s.substr(l+1,r-l);
        
        r = l;
        
        while (l >= 0 && s[l] == ' ') {
          l--;  
        }
        if (r-l > 0 && res != "" && l >= 0) {
          res += ' ';
        }
        r = l;
        
      }

      return res;
    }
};
