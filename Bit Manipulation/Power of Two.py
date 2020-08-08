class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 0:
            return 0
        n = bin(n)
        n = str(n)
        if n.count('1') == 1:
            return 1
        return 0

#---------------------Solution2---------------# using Bitwise Operators


if n == 0:
            return 0

        if n & (n-1)==0:
            return 1
        return 0
