class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        res = []
        
        for i in nums1:
            if i in nums2 and i not in res:
                res.append(i)

        return res
