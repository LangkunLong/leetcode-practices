class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # pretty confusing question
        # kadanane's algorithm, at each value do we set current array as the maximum subarray or pick the value itself
        # for going around: maximum is just the total value removing the negative portion (total - global min)
        # for noraml traversal: maximum is current max. (same as previous question)
        
        if not nums:
            return 0
        
        cur_max, glo_max = 0, nums[0]
        cur_min, glo_min = 0, nums[0]
        total = 0
        for val in nums:
            if cur_max + val > 0:
                cur_max += val
                glo_max = max(glo_max, cur_max)
            else:
                cur_max = 0
                glo_max = max(glo_max, val)
            if cur_min + val < 0:
                cur_min += val
                glo_min = min(glo_min, cur_min)
            else:
                cur_min = 0
                glo_min = min(glo_min, val)
            total += val
        
        # if all negatives
        if glo_max < 0:
            return glo_max
        else:
            return max((total - glo_min, glo_max))
