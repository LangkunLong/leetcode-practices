class Solution:
    def findMin(self, nums: List[int]) -> int:
        # array is rotated left, find min element in logn time
        # if we find a midpoint where it is larger than its right value, then the next value is start of rotation
        # if not we keep going left

        def helper(l,r):
            if l > r:
                return nums[l]
            m = (l + r) // 2
            if nums[m] > nums[m+1]:
                return nums[m+1]
            else:
                left = helper(l, m-1)
                return left
        
        return helper(0, len(nums) - 1)
