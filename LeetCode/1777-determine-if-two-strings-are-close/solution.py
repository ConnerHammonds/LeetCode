class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
      if len(word1) != len(word2) or set(word1) != set(word2):
        return False

      freq1 = [0] * 26
      freq2 = [0] * 26

      for i in range(len(word1)):
        freq1[ord(word1[i]) - ord('a')] += 1

      for i in range(len(word2)):
        freq2[ord(word2[i]) - ord('a')] += 1
      
      freq1.sort()
      freq2.sort()

      if freq1 == freq2:
        return True

      return False
