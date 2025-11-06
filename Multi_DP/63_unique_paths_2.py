class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # recursive dfs?
        row, col = len(obstacleGrid), len(obstacleGrid[0])
        def dfs(r, c):
            if r == row or c == col or obstacleGrid[r][c] == 1:
                return 0
            if r == row -1 and c == col -1:
                return 1

            return dfs(r+1, c) + dfs(r, c+1)
        
        return dfs(0,0)
