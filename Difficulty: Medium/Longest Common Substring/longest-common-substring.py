class Solution:
    def longCommSubstr(self, text1, text2):
        # code here
        dp = [[-1 for i in range(len(text2) + 1 )] for j in range(len(text1) + 1 )]

        for i in range(len(text1) + 1):
            dp[i][0] = 0
        for i in range((len(text2) + 1)):
            dp[0][i] = 0
        ans = 0
        for i in range(1, len(text1) + 1):
            for j in range(1, len(text2) + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                    ans = max(ans, dp[i][j])
                    continue
                dp[i][j] = 0


        return ans