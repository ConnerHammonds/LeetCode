class Solution:
    def maximumSubarraySum(self, nums: list[int], k: int) -> int:
      count = defaultdict(int) 
      l = 0
      maxSum = 0
      currSum = 0
      length = 0

      for i in range(len(nums)):
        length += 1
        count[nums[i]] += 1
        currSum += nums[i]

        while count[nums[i]] > 1 or length > k:
          count[nums[l]] -= 1
          currSum -= nums[l]
          length -= 1
          l += 1
        
        if length == k:
          maxSum = max(maxSum, currSum)
        
      return maxSum
