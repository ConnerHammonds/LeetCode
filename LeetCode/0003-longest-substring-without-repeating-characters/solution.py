class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
      charSet = set()
      maxLen = 0
      l = 0

      for r in range(len(s)):
        while s[r] in charSet:
          charSet.remove(s[l])
          l += 1

        charSet.add(s[r])
        currAns = len(charSet)
        if currAns > maxLen:
          maxLen = currAns
      
      return maxLen

        

        


