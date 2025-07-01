class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # no hash, O(n^2) brute force traversal, 
        # i know array is sorted, so every element to the right will be larger
        # 2 pointer approach, if start + end > total, move end_ptr to the left:
        start_ptr, end_ptr = 0, len(numbers) - 1
        while start_ptr < end_ptr:
            if numbers[start_ptr] + numbers[end_ptr] == target:
                return [start_ptr + 1, end_ptr + 1]
            elif numbers[start_ptr] + numbers[end_ptr] > target:
                end_ptr -= 1
            elif numbers[start_ptr] + numbers[end_ptr] < target:
                start_ptr += 1
        