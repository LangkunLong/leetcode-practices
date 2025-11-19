class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        #using 2 pointer approach:
        if not nums:
            return 0
        if len(nums) == 1:
            return 1 if nums[0] == k else 0
        
        l = 0
        res = 0
        cur_sum = nums[0]
        for r in range(1, len(nums)):
            cur_sum += nums[r]
            while cur_sum >= k:
                if cur_sum == k:
                    res += 1
                    break
                cur_sum -= nums[l]
                l += 1

        return res
