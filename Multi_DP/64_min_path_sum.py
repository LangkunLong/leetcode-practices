class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # bottom up approach start from bottom right and work to top left
        dp = grid
        for i in range(len(grid)-1, -1, -1):
            for j in range(len(grid[i])-1, -1, -1):
                if i + 1 < len(grid) and j + 1 < len(grid[i]):
                    dp[i][j] += min(dp[i][j+1], dp[i+1][j])
                elif i + 1 < len(grid):
                    dp[i][j] += dp[i+1][j]
                elif j + 1 < len(grid[i]):
                    dp[i][j] += dp[i][j+1]
        return dp[0][0]

