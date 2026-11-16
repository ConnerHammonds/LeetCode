class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
      freq = defaultdict(int)

      for num in arr:
        freq[num] += 1
      
      return len(freq.values()) == len(set(freq.values()))
