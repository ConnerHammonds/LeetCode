class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        #[0, 2, 4, 6, 8, 10]      target = 8
        #l = 0, m = 3, r = 5
        # l        m      r

        #          l  m   r
        while l <= r:
            m = (l + r) // 2
            if target == nums[m]:
                return m
            elif target > nums[m]:
                l = m + 1
            elif target < nums[m]:
                r = m - 1

        return -1


