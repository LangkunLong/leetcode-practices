
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        tot_sum = nums[0]
        cur_sum = 0
        for i in range(len(nums)):
            if cur_sum + nums[i] >= 0:
                cur_sum += nums[i]
                tot_sum = max(tot_sum, cur_sum)
            else:
                cur_sum = 0
                tot_sum = max(tot_sum, nums[i]) # could meet a less negative number
        
        return tot_sum
