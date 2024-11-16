class Solution:
    def maxArea(self, height: List[int]) -> int:
        # similar to trapping rainwater, except here we are finding the maximum enclosed area so don't have to worry about left and right max, we can calculate max_area using min(left_height, right_height) * dist(right-left)
        
        max_area = 0
        start, end = 0, len(height) - 1
        while start < end:
            dist = end - start
            max_area = max(max_area, dist*min(height[start], height[end]))
            if height[start] > height[end]:
                end -= 1
            else:
                start += 1
        return max_area