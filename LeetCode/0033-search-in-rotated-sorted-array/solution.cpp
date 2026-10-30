class Solution {
public:
    int search(vector<int>& nums, int target) {
      if (nums.size() == 1 && nums[0] == target) {return 0;} 
      else if (nums.size() == 1 && nums[0] != target) {return -1;}

      int l = 0;
      int r = nums.size() - 1;
      int prev = 0;
      int split = -1;

      //find rotation
      for (int i = 1; i < nums.size(); i++) {
        if (nums[i] < nums[prev]) {
          split = i;
        }
        prev++;
      }

    //if arr is rotated, prep l, split, and r for binary search
     if (split != -1) { 
      if (target > nums[l]) {
          r = split;
          split = (l+r) / 2;
        }
        else if (target < nums[l]) {
          l = split;
          split = (l+r) / 2;
        }
        else if (target == nums[l]) {return l;}
     }
        
      //if arr isn't rotated, set split to mid and run binary search
      if (split == -1) {split = (l+r) / 2;}

      //normal binary search
      while (l <= r) {
        
        if (target > nums[split]) {
          l = split+1;
          split = (l+r) / 2;
        }
        else if (target < nums[split]) {
          r = split-1;
          split = (l+r) / 2;
        }
        else if (target == nums[split]) {return split;}
      }
      return -1;
    }
};
