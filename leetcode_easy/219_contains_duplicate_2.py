class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # nums[i] == nums[j], abs(i-j) <= k
        # distance between i and j must be less or equal than k
        # easier to use a dictionary to store the index, and update to biggest index if does not meet abs value
        if k == 0:
            return False
        indice_map = dict()
        for i, num in enumerate(nums):
            if num in indice_map:
                if abs(i - indice_map[num]) <= k:
                    return True
                else:
                    indice_map[num] = i
            else:
                indice_map[num] = i
        return False
