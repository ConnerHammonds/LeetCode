class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
      i = inf
      j = inf

      for num in nums:
        if num <= i:
          i = num
        elif num <= j:
          j = num
        else:
          return True
      
      return False
        


