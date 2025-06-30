class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # all triplets that sums up to 0, no duplicate triplets
        # if we fix 1 numbers, we are left with 2 sum problem:
        # unsorted, so need a hash for lookup
        if len(nums) < 3:
            return []
        if len(nums) == 3:
            if sum(nums) == 0:
                return [nums]
            else:
                return []

        nums = sorted(nums)
        solutions = []
        for i in range(len(nums)-1):
            # avoid duplicate fixed number
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            start, end = i+1, len(nums) - 1
            # using 2 pointer approach as hashtable is not effificent with triplets, can have duplicate entries in the hash because only can store result from subtracting 2 numbers, the last number can be duplicates 
            while start < end:
                three_sum = nums[i] + nums[start] + nums[end]
                if three_sum == 0:
                    solutions.append([nums[i], nums[start], nums[end]])
                    # need to skip over duplicates with same values as [start] and [end]
                    while start < end and nums[start] == nums[start+1]:
                        start += 1
                    while start < end and nums[end] == nums[end-1]:
                        end -= 1
                    start += 1
                    end -= 1
                elif three_sum < 0:
                    start += 1
                elif three_sum > 0:
                    end -= 1
        return solutions

        
