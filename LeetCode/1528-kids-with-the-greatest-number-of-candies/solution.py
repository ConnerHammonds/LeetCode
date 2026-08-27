class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        res = []
        m = 0

        for i in candies:
            if i > m:
                m = i

        for i in range(len(candies)):
            if candies[i] + extraCandies >= m:
                res.append(True)
            else:
                res.append(False)
        return res
