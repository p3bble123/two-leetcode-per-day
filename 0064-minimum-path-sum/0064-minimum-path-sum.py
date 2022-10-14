class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rowLen = len(grid)
        colLen = len(grid[0])

        dp = []

        for row in range(rowLen):
            dp.append([0] * colLen)

        dp[0][0] = grid[0][0]

        for col in range(1, colLen):
            dp[0][col] = dp[0][col - 1] + grid[0][col]

        for row in range(1, rowLen):
            dp[row][0] = dp[row - 1][0] + grid[row][0]

        for row in range(1, rowLen):
            for col in range(1, colLen):
                dp[row][col] = min(dp[row][col - 1], dp[row - 1][col]) + grid[row][col]

        return dp[rowLen - 1][colLen - 1]

