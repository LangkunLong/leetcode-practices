def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
    # pattern repeats in right -> down -> left -> up 
    # keep track of top, bottom, left and right boundaries, every time we finish traversing 1 direction, update boundary
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1
    if not matrix:
        return []
    spiral = []
    while left <= right and top <= bottom: 
        # traverse from left to right
        for i in range(left, right+1):
            spiral.append(matrix[top][i])
        top += 1

        # traverse from top to bottom
        for i in range(top, bottom+1):
            spiral.append(matrix[i][right])
        right -= 1

        # right to left
        if top <= bottom:
            for i in range(right, left-1, -1):
                spiral.append(matrix[bottom][i])
            bottom -= 1 

        #bottom to top
        if left <= right:
            for i in range(bottom, top-1, -1):
                spiral.append(matrix[i][left])
            left += 1

    return spiral