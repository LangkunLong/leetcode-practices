class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # cannot use sliding window because array contains negative numbers
        # simply adding/ removing does not necessarily mean we are increasing / decreasing the size
        prefix_map = {0:1}
        cur_sum = 0
        res = 0
        for num in nums:
            cur_sum += num
            # at current position, how mnay subarrays we can get that sum up to k? we can remove a prefix sum of
            # (cur_sum -k) to sum to k, and we have a count of that prefix sum
            if cur_sum - k in prefix_map:
                res += prefix_map[cur_sum-k]
            if cur_sum not in prefix_map:
                prefix_map[cur_sum] = 1
            else:
                prefix_map[cur_sum] += 1
        return res
