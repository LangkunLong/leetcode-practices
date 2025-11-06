class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # recursive dfs, add cachingL unique paths at position [i] is unique paths from position [i+1] and [j+1]
        row, col = len(obstacleGrid), len(obstacleGrid[0])
        dp = {(row-1, col-1):1}
        def dfs(r, c):
            if r == row or c == col or obstacleGrid[r][c] == 1:
                return 0
            if (r, c) in dp:
                return dp[(r,c)]

            dp[(r,c)] = dfs(r+1, c) + dfs(r, c+1)
            return dp[(r,c)]
        
        return dfs(0,0)
