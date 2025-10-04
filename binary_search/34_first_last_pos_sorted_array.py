class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # non-decreasing order => increasing with duplicates
        # just call binary search twice, find lower and upper bound
        
        def helper(l, r, lowerBound):
            i = -1
            while l <= r:
                m = (l + r) //2
                if nums[m] == target:
                    i = m
                    # need to keep looking through left/right index to find lower/upper bound
                    if lowerBound:
                        r = m - 1
                    else:
                        l = m + 1
                elif target > nums[m]:
                    l = m + 1
                else:
                    r = m -1
            return i
        left = helper(0, len(nums)-1, True)
        right = helper(0, len(nums)-1, False)

        return [left, right]
        
