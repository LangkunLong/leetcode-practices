class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # problem here is that array is shifted, so need original sorted order
        # recursively search, if we cannot find target in the 'expected' search space, try the other half
        # divide and conquer O(2*log(n)) => O(log(n))
        l,r = 0, len(nums) - 1
        found = [-1]
        def recurse(l, r):
            if l > r:
                return 
            m = (l + r) //2
            if nums[m] == target:
                found[0] = m
        
            recurse(l, m-1)
            recurse(m+1, r)
        
        recurse(0, len(nums) - 1)
        return found[0]



            
