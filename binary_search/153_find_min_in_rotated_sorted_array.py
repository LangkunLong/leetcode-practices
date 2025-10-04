class Solution:
    def findMin(self, nums: List[int]) -> int:
        # array is rotated left, find min element in logn time
        # need to satisy nums[l] <= nums[m] <= nums[r] to see if we are in unrotated portion
        l, r = 0, len(nums) - 1
        res = [nums[0]]

        def helper(l,r):
            if l > r:
                return 
            m = (l + r) // 2
            res[0] = min(res[0], nums[m])
            if nums[l] <= nums[m] and nums[m] <= nums[r]:
                helper(l, m-1)
            else:
                if nums[l] > nums[m]:
                    helper(l, m-1)
                else:
                    helper(m+1, r)
        helper(l, r)
        
        return res[0]
