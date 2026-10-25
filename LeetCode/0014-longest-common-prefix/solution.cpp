class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
      if (strs.size() == 0) return "";
      string ans = strs[0];

      for (int i = 0; i < strs.size(); i++) {
        string curr = "";
        for (int j = 0; j < strs[i].size() && j < ans.size(); j++) {
          if (strs[i][j] != ans[j]) {
            break;
          }
          else {
            curr += strs[i][j];
          }
        }
        if (curr.size() < ans.size()) ans = curr;
      }
      return ans;
    }
};
