class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1]:
            return 0

        dp, rowLen, colLen = [], len(obstacleGrid), len(obstacleGrid[0])

        for row in range(rowLen):
            dp.append([0] * colLen)
        dp[0][0] = 1

        for row in range(rowLen):
            if obstacleGrid[row][0] == 1:
                dp[row][0] = -2
                break
            dp[row][0] = 1

        for col in range(colLen):
            if obstacleGrid[0][col] == 1:
                dp[0][col] = -2
                break
            dp[0][col] = 1

        for row in range(1, rowLen):
            for col in range(1, colLen):
                if obstacleGrid[row][col] == 1 or (dp[row - 1][col] == -2 and dp[row][col - 1] == -2):
                    dp[row][col] = 0
                    continue

                if dp[row - 1][col] == -2:
                    dp[row][col] = dp[row][col - 1]
                elif dp[row][col - 1] == -2:
                    dp[row][col] = dp[row - 1][col]
                else:
                    dp[row][col] = dp[row - 1][col] + dp[row][col - 1]

        return dp[-1][-1]
