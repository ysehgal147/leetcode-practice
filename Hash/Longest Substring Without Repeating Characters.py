class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        temp = ''
        mx = 0
        for i in s:
            if i not in temp:
                temp += i
            else:
                mx = max(mx, len(temp))
                temp += i
                temp = temp[temp.index(i) + 1:]
        return max(mx, len(temp))
