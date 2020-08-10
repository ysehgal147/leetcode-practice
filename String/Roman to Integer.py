class Solution:
    def romanToInt(self, s: str) -> int:
        key = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        count = 0
        for i in range(0, len(s)-1):
            if key[s[i]] < key[s[i+1]]:
                count -= key[s[i]]
            else:
                count += key[s[i]]
        return count + key[s[-1]]
