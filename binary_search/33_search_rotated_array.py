class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # need to determine for each subarray the middle value is in left-sorted, or right-sorted
        l,r = 0, len(nums) - 1

        while l <= r:
            m = (l+r) // 2
            if target == nums[m]:
                return m
            # middle in left-sorted array
            if nums[l] <= nums[m]:
                if target < nums[l]:
                    l = m +1
                elif target < nums[m]:
                    r = m -1
                else:
                    l = m+1
            else:
                if target > nums[r]:
                    r = m-1
                elif target > nums[m]:
                    l = m+1
                else:
                    r = m-1
        return -1



            
