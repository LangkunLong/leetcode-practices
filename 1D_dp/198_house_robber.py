class Solution:
    def rob(self, nums: List[int]) -> int:
        # starting at base case, only 2 houses (n - 2)
        # at each step compare between (house[i] + house[i-2]) or house[i-1]

        if len(nums) < 3:
            if len(nums) == 1:
                return nums[0]
            else:
                return max(nums[0], nums[1])
        
        dp = nums
        # maintains the maximum we can rob up to each house: at house 2 the max we can get is from robbing only 1 house
        # so pick the maximum
        dp[1] = max(dp[0], dp[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2] + dp[i])

        return dp[-1]       

