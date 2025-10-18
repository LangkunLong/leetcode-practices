class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # using stack, if encounter a smaller height, means we cannot extend the previous height, so we find the current max
        # area; since the current height is smaller, we can extend it to the left
        # we pop the stack if we encounter the smaller height, and push the new element with a new starting index (extend starting index to the left)
        # in the stack, keep track of its height, and maximum starting position
        # extend the starting position by seeing how many elements we pop from the stack (how many are bigger than cur height)
