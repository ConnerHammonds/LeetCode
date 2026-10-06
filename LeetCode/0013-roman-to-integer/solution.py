class Solution:
    def romanToInt(self, s: str) -> int:
        res = []

        for i in s:
            match i:
                case "I":
                    res.append(1)
                case "V":
                    res.append(5)
                case "X":
                    res.append(10)
                case "L":
                    res.append(50)
                case "C":
                    res.append(100)
                case "D":
                    res.append(500)
                case "M":
                    res.append(1000)

        for i in range(len(res) - 1):
            if res[i] < res[i+1]:
                res[i] = -res[i]

        return sum(res)
