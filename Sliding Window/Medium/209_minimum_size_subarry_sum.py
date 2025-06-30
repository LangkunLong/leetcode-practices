class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # sliding window
        left = 0
        window_size = float(inf)
        window_sum = 0
        for right in range(len(nums)):
            window_sum += nums[right]
            # if sum >= target, start moving left pointer to try minize window size 
            while window_sum >= target:
                window_size = min(window_size, right-left + 1)
                window_sum -= nums[left] # have to subtract the sum first before moving the pointer
                left += 1
            
        return 0 if window_size == float(inf) else window_size
