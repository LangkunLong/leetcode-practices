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

        # O(1) memory approach:
        # only need to keep track of rob1, rob2, values indicating best 
        # rob1 is maximum of robbing up until 2 houses before
        # rob2 is maximum of robbing up until previous house
        rob1, rob2 = 0, 0
        # [rob1, rob2, cur (i), i + 1, i+2,...]
        for num in nums:
            tmp = max(rob1 + num, rob2)
            rob1 = rob2
            rob2 = tmp
        return rob2

