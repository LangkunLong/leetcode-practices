class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:  # Handle empty input
            return 0
        
        # 2 pointer appoach re-do:
        left_ptr, right_ptr = 0, len(height) - 1
        left_max, right_max = height[left_ptr], height[right_ptr]
        water = 0

        while left_ptr < right_ptr:
            # process whichever side is lower
            if height[left_ptr] < height[right_ptr]:
                if height[left_ptr] >= left_max:
                    left_max = height[left_ptr]
                water += left_max - height[left_ptr]
                left_ptr += 1
            else:
                if height[right_ptr] >= right_max:
                    right_max = height[right_ptr]
                water += right_max - height[right_ptr]
                right_ptr -= 1
        return water
