# initial approach using bottom up dp
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # at each position, if next element is smaller, we accept next element's longest subsequence, because it is for sure
        # longer then starting at current position; if current value is smaller, start a new subsequence and find the biggest 
        # element it is smaller to in the preceding array 
        dp = [0] * (len(nums))
        dp[len(nums)-1] = 1
        ind_mapper = dict()
        
        for idx, num in enumerate(nums):
            ind_mapper[num] = idx
        
        for i in range(len(nums)-2, -1, -1):
            if nums[i] > nums[i+1]:
                dp[i] = dp[i-1]
            else:
                smallest_idx = self.bs_helper(nums[i+1:], nums[i])
                dp[i] = max(dp[i], 1 + dp[smallest_idx])
        return dp[0]


    def bs_helper(self, nums, target):
        smallest_val = float('inf')
        for idx, n in enumerate(nums):
            if target < n:
                if n < smallest_val:
                    smallest_val = min(smallest_val, n)

        return ind_mapper[smallest_val] 
