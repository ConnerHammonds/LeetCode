class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        set<int> res;
        vector<int> vec;

        for (int i = 0; i < nums1.size(); i++) {
          auto iterator = find(nums2.begin(), nums2.end(), nums1[i]);
          if (iterator != nums2.end()) res.insert(nums1[i]);
        }
        vec.assign(res.begin(), res.end());
        return vec;
    }
};
