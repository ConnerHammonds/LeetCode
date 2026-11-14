class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
      res = []
      greatest = 0
      for num in candies:
        greatest = max(greatest, num)

      for num in candies:
        if num + extraCandies >= greatest:
          res.append(True)
        else:
          res.append(False)
      
      return res

        
