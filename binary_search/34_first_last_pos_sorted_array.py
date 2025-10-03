class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # non-decreasing order => increasing with duplicates
        # just call binary search twice, find position of target and target + 1 (start_pos of next bigger val) and - 1
        sol = [-1, -1]
        l, r = 0, len(nums) - 1
        # find start pos    
        while l <= r:
            m = (l+r) // 2
            if nums[m] == target:
                sol[0] = m
            elif target > nums[m]:
                l = m + 1
            else:
                r = m - 1

        if sol[0] == -1:
            return sol
        
        l, r = 0, len(nums) - 1
        # find second   
        while l <= r:
            m = (l+r) // 2
            if nums[m] == t:
                sol[1] = m - 1
            elif target > nums[m]:
                l = m + 1
            else:
                r = m - 1
        
