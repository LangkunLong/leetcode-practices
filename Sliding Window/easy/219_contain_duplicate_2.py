# defintely not easy, difficult to grasp concept
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # duplicate -> use hash
        # see a range -> likely sliding window

        l = 0
        duplicate = set()
        for r in range(len(nums)):
            if abs(l-r) <= k:
                if nums[r] in duplicate:
                    return True
                else:
                    duplicate.add(nums[r])
            else:
                duplicate.remove(nums[l])
                l += 1
                if nums[r] in duplicate:
                    return True
                else:
                    duplicate.add(nums[r])
        return False

