class Solution {
public:
    int pivotIndex(vector<int>& nums) {
      int sum = 0;
      int curSum = 0;

      for (int i: nums)
        sum += i;
      
      for (int i = 0; i < nums.size(); i++) {
        curSum += nums[i];
        if (curSum == sum) {return i;}
        sum -= nums[i];

      }

      return -1;
    }
};
