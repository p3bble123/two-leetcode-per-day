class Solution:
    def twoEggDrop(self, n: int) -> int:

        # basically the same solution as 887-super-egg-drop,
        # just change egg limit to 2 instead of n

        dp = [[0 for j in range(3)] for i in range(n + 1)]

        for floor in range(1, n + 1):
            for egg in range(1, 3):
                dp[floor][egg] = 1 + dp[floor - 1][egg] + dp[floor - 1][egg - 1]
                if dp[floor][egg] >= n:
                    return floor