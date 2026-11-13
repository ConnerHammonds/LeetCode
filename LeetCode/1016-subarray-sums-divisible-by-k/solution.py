class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
      count = 0 
      pre = 0
      freq = [1] + [0] * k
             
      for num in nums:
        pre = (pre + num) % k #current remainder of prefix after modulo k
        count += freq[pre] #add the value in the freq array that is equal to that remainder
        freq[pre] += 1 #update freq array
      
      return count
