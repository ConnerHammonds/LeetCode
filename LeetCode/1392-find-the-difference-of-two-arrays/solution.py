class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:

      res = [[], []]

      freq = defaultdict(int)

      for num in nums2:
        freq[num] += 1

      for num in nums1:
        if freq[num] == 0:
          res[0].append(num)
          freq[num] = 67
    
      freq = defaultdict(int)

      for num in nums1:
        freq[num] += 1

      for num in nums2:
        if freq[num] == 0:
          res[1].append(num)
          freq[num] = 67
      
      return res

