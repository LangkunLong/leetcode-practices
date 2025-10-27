class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # base case is last index, can form a subsequence of 1
        # go from last index to first, check all preceding indices, see if we can attach current subsequence to previous
        # subsequence only if current value is smaller
        # dp[0] represent the longest increasing subsequence starting at index 0, cannot just assume dp[0] is the longest
        # need to return max(dp)

        LIS = [1] * len(nums)
        for i in range(len(nums)-1, -1, -1):
            for j in range(i, len(nums)):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])
        return max(LIS)

