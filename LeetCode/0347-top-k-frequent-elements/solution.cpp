class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> map; // nums element is key, frequency is value
        vector<vector<int>> bucket(nums.size() + 1);
        vector<int> ans;

        //create frequency map
        for (int i = 0; i < nums.size(); i++) {
          
            if (!map.contains(nums[i])) map.insert({nums[i], 0});

          map.at(nums[i]) += 1;
        }

      // add to buckets
      for (auto pair : map) {
        bucket[pair.second].push_back(pair.first);
      }

      // iterate from the back of the bucket sorted vector
      // add numbers to the ans vector and decrement k each time a number is added
      int end = bucket.size() - 1;
      while (k > 0) {
        if (!bucket[end].empty()) {
          for (int num : bucket[end]) {
            ans.push_back(num);
            k--;
          }
        }
        end--;
      }
      return ans;
    }
};
