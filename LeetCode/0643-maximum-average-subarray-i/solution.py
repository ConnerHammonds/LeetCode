class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
      l = 0
      r = k
      maxSum = sum(nums[:k])
      currSum = maxSum
      
      
      while r < len(nums):
        currSum -= nums[l]
        l += 1
        currSum += nums[r]
        r += 1
        maxSum = max(maxSum, currSum)

      return maxSum / k
