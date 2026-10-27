class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        unordered_map<int, int> map {{0, 1}};
        int tot = 0;
        int sum = 0;

        for (int i = 0; i < nums.size(); i++) {
            sum += nums[i];

            if (map.contains(sum - k)) {
                tot += map[sum - k];
            }

            map[sum]++;
        }

        return tot;
    }
};
