class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp={}
        def LCS(text1,text2):
            if len(text1)==0 or len(text2)==0:
                return 0
            if (len(text1),len(text2)) in dp:
                return dp[(len(text1),len(text2))]
            if text1[-1] == text2[-1]:
                return 1 + LCS(text1[:-1], text2[:-1])
            else:
                dp[(len(text1),len(text2))] = max(LCS(text1[:-1], text2), LCS(text1,text2[:-1]))
                return dp[(len(text1),len(text2))]
        return LCS(text1,text2)

#---------------------Solution2------------------------#

        n, m = len(text1), len(text2)
        dp = [[0]*(m+1) for _ in range(n+1)]
        for i in range(n):
            for j in range(m):
                if text1[i] == text2[j]:
                    dp[i+1][j+1] = dp[i][j]+1
                else:
                    dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
        return dp[-1][-1]
