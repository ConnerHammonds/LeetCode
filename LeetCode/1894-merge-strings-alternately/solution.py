class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
      shorter = min(len(word1), len(word2))
      longer = max(len(word1), len(word2))
       
      if len(word1) == longer:
        long_word = word1
      else:
        long_word = word2
      diff = longer - shorter
      res = ''


      for i in range(shorter):
        res += word1[i]
        res += word2[i]
      
      for i in range(shorter, longer):
        res += long_word[i]
      
      return res
