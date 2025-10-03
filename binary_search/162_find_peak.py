class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # always go towards to the greater value, we have 2 cases:
        # for the next value, if it is still not a peak element, we keep going towards the bigger side and eventuall reahches 
        # a boundary [1,2,3,4] -> 4 is a peak
        # if we encounter a smaller value, then cur value is a peak [1,2,3,1] -> 3 is a peak
        if len(nums) == 1:
            return 0

        l,r = 0, len(nums) - 1
        while l <= r:
            m = (l+r) // 2
            if m > 0 and nums[m] < nums[m-1]:
                r = m -1
            elif m < len(nums) - 1 and nums[m] < nums[m+1]:
                l = m + 1
            else:
                return m
        
        return 0
                
