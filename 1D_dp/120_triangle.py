class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # base case, reaching the leaf node
        # each time we move down the triangle there are 2 choices, lowest path sum at i, or lowest path sum at i + 1
        # or at each layer we just take the minimum
        res = 0
        for layer in triangle:
            min_cost = min(layer)
            res += min_cost
        return res
