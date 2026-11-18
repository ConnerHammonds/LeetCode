class Solution:
    def maxVowels(self, s: str, k: int) -> int:
      l = 0
      r = k
      max_count = 0
      count = 0
      length = 0

      vowels = {'a', 'e', 'i', 'o', 'u'}

      for r in range(len(s)):
        length += 1
        if s[r] in vowels:
          count += 1
          
        
        while length > k:
          if s[l] in vowels:
            count -= 1
          l += 1
          length -= 1

        max_count = max(count, max_count)
        
      return max_count
