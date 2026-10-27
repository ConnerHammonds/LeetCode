
class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        if (nums.empty()) {
            return 0;
        }

        int maxLen = 1;
        unordered_set<int> hset;

        for (int num : nums) {
            hset.insert(num);
        }

        for (int i : hset) {
            auto it = hset.find(i - 1);

            if (it == hset.end()) {
                int len = 1;
                it = hset.find(i + 1);
                while (it != hset.end()) {
                    len++;
                    i++;
                    it = hset.find(i + 1);
                }
                if (len > maxLen) maxLen = len;
            }
        }

        return maxLen;
    }
};

