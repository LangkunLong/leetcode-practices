class Solution:
    def findMin(self, nums: List[int]) -> int:
        # array is rotated left, find min element in logn time
        # divide and conquer to find left min and right min
        res = [nums[0]] # set initial value 

        def helper(l,r):
            if l > r:
                return 
            m = (l + r) // 2
            res[0] = min(res[0], nums[m])
            l_min = helper(l, m-1)
            r_min = helper(m+1, r)
        
        helper(0, len(nums) - 1)
        return res[0]
