class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # using stack, if encounter a smaller height, means we cannot extend the previous height, so we find the current max
        # area; since the current height is smaller, we can extend it to the left
        # we pop the stack if we encounter the smaller height, and push the new element with a new starting index (extend starting index to the left)
        # in the stack, keep track of its height, and maximum starting position
        # extend the starting position by seeing how many elements we pop from the stack (how many are bigger than cur height)

        maxArea = 0
        stack = []
        for i in range(len(heights)):
            start = i
            while stack and heights[i] < stack[-1][1]:
                p_start, p_height = stack.pop()
                prevArea = (i - p_start) * p_height
                maxArea = max(maxArea, prevArea)
                start = p_start # can extend starting index to the popped element's start index, since it is smaller    
            stack.append( (start, heights[i]))
        
        # if still left over
        while stack:
            start, height = stack.pop()
            curArea = (len(heights) - start) * height
            maxArea = max(maxArea, curArea)
        
        return maxArea
            


            

