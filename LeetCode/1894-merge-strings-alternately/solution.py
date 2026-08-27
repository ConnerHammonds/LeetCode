class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        p1 = 0
        p2 = 0
        res = []
        longer = max(len(word1), len(word2))

        if len(word1) == longer:
            longest = word1
        else:
            longest = word2

        while p1 < len(word1) and p2 < len(word2):
            res.append(word1[p1])
            p1 += 1
            res.append(word2[p2])
            p2 += 1
        
        res.append(longest[p1:])
        
        res = "".join(res)
        return res
