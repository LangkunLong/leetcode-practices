class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # no matrix
        if not matrix:
            return False
        
        # out of bonds
        if target > matrix[len(matrix)-1][len(matrix[0])-1] or target < matrix[0][0]:
            return False
        
        # binary search row values, then binary search col values
        l_row, r_row = 0, len(matrix) - 1
        while l_row <= r_row :
            r_mid = (l_row + r_row) // 2
            print("row", matrix[r_mid][0])
            if matrix[r_mid][0] == target:
                return True
            elif target > matrix[r_mid][0]:
                l_row = r_mid + 1
            else:
                r_row = r_mid - 1
        
        # manually removing, not generic
        l_row -= 1 # exit l > r, its when l == r (mid = l) and we set l = r + 1, so we backtrack to last valid row 

        # if we are here, found the row to look for
        l_col, r_col = 0, len(matrix[l_row]) - 1
        while l_col <= r_col:
            m_col = (l_col + r_col) // 2
            print("col", matrix[l_row][m_col])
            if matrix[l_row][m_col] == target:
                return True
            elif target > matrix[l_row][m_col]:
                l_col = m_col + 1
            else:
                r_col = m_col -1
        
        return False
