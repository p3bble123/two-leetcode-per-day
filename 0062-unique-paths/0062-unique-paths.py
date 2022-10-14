class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = []

        for row in range(m):
            dp.append([0] * n)

        dp[0][0] = 1

        for row in range(1, m):
            dp[row][0] = 1

        for col in range(1, n):
            dp[0][col] = 1

        for row in range(1, m):
            for col in range(1, n):
                dp[row][col] = dp[row - 1][col] + dp[row][col - 1]

        return dp[-1][-1]


