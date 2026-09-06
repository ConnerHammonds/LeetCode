class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = strs[0]

        for word in strs:
            p = 0
            while p < len(word) and p < len(res) and word[p] == res[p]:
                p += 1
            res = word[0:p]
        
        return res

