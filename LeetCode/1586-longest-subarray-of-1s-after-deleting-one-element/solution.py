class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
      res = 0
      can_delete = True
      l = 0
      

      for r in range(len(nums)):
        if nums[r] == 0 and can_delete == True:
          can_delete = False
        
        elif nums[r] == 0 and can_delete == False:
          
          while can_delete == False:
            if nums[l] == 0:
              l+=1
              break
            l += 1
            
        res = max(res, r-l)

      return res

