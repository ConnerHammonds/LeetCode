class Solution {
public:
    int search(vector<int>& nums, int target) {
        int l = 0;
        int r = size(nums) - 1;

        while (l <= r) {
            int m = (l + r) / 2;
            if (target > nums[m]) {
                l = m + 1;
                m = (l + r) / 2;
            }
            else if (target < nums[m]) {
                r = m - 1;
                m = (l + r) / 2;
            }
            else if (target == nums[m]) {
                return m;
            }
        }
        return -1;
    }
};
