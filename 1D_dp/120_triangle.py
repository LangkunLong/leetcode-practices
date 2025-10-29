class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # base case, reaching the leaf node
        # each time we move down the triangle there are 2 choices, lowest path sum at i, or lowest path sum at i + 1
        # using O(n^2) memory, how to solve using O(n) space?
        dp = [[num for num in layer] for layer in triangle]
        #print(dp)
        for i in range(len(triangle)-2, -1, -1):
            for j in range(len(triangle[i])):
                dp[i][j] += min(dp[i+1][j], dp[i+1][j+1])
        print(dp)
        return dp[0][0]

        # O(n) memory, only need to keep information from the previous row:
        dp = triangle[-1][:]  # start from the last row
        
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                dp[j] = triangle[i][j] + min(dp[j], dp[j + 1])
        
        return dp[0]
