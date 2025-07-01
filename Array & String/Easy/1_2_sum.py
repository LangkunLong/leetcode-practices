class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if nums == None:
            return []
        if len(nums) == 1:
            return []

        # cannot use 2 pointer appraoch because array is not sorted, and need order of elements so cannot sort array

        # have to use dictionary appraoch:
        num_to_indic_dict = dict()
        for i, num in enumerate(nums):
            remainder = target - num
            if remainder in num_to_indic_dict:
                return [i, num_to_indic_dict[remainder]]
            num_to_indic_dict[num] = i
