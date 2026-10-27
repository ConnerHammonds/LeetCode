class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        vector<int> seen;

        for (int i = 0; i < nums.size(); i++) {
          if (find(seen.begin(), seen.end(), nums[i]) == seen.end()) {seen.push_back(nums[i]);}
          else {nums.erase(nums.begin() + i); i--;}
        }

      return nums.size();
    }
};
