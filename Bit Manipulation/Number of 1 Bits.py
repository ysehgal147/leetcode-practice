class Solution:
    def hammingWeight(self, n: int) -> int:
        n = bin(n)
        n = str(n)
        return n.count('1')
