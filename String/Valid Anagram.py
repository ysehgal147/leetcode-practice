class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return 0
        x = s+t
        s = list(s)
        t = list(t)
        for i in x:
            if (i in s) and (i in t):
                s.remove(i)
                t.remove(i)
        if len(s) == 0 and len(t) == 0:
            return 1
        return 0

#---------------------Solution2--------------------#

        if len(s) != len(t):
            return 0
        return sorted(s) == sorted(t)
