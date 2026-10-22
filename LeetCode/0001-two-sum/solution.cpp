class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
      unordered_map<int, int> seen; // values are key, indices are the value

      for (int i = 0; i < nums.size(); i++) {
        int complement = target - nums[i];

        if (seen.contains(complement)) { 
          int j = seen[complement];
          return {i, j};
        }
        seen.insert({nums[i], i});
      }
      return {};
    }
};
