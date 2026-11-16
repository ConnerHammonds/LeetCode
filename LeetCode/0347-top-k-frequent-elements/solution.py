class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
      nums = sorted(nums)
      l = 0
      curr_count = 0
      mp = defaultdict(int)
      res = []

      for i in range(len(nums)):
        
        if nums[i] != nums[l]:
          curr_count = 1
          l = i
        
        mp[nums[i]] += 1
      
      sorted_data = dict(sorted(mp.items(), key=lambda item: item[1], reverse=True))

      for key in sorted_data.keys():
        if k > 0:
          res.append(key)
          k -= 1
        else:
          break
      
      return res
        
