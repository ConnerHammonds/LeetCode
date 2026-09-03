class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        arr = []
        p1 = 0
        p2 = 0
        #initialize two pointers at the beginning of each string
        #if s[p1] == t[p2], append to arr and then move them both over.
        #if not equal, move p2 over
        #continue until all the way through t
        #join arr with res = "".join(arr)
        #if res = s, return true, else return false

        #return true if s is ""
        if not s:
            return True

        while p2 < len(t) and p1 < len(s):
            if s[p1] == t[p2]:
                arr.append(t[p2])
                p1 += 1
                p2 += 1
            else:
                p2 += 1

        res = "".join(arr)
        if res == s:
            return True
        else:
            return False


