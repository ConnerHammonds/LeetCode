class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
      mp = {}

      for i in range(len(s)):
        #if key is not in map, add the key val pair
        if s[i] in mp and mp[s[i]] != t[i]:
          return False
        mp[s[i]] = t[i]
        #if it is in the map and it's not equal to the current value, return false
        if s[i] in mp and mp[s[i]] != t[i]:
            return False

      sets = set(mp.values())
      print(sets)
      print(mp)
      if len(sets) != len(mp.values()):
        return False
    
      return True
