class Solution {
public:
    int largestAltitude(vector<int>& gain) {
      int max = 0;
      int pre = 0;
      for (int i : gain) {
        pre += i;
        if (pre > max) max = pre;
      } 
      return max;
    }
};
