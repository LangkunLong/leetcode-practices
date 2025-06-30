class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # O(m + n) solution, record row and columns that needs to be set to zero
        # zero_rows = set()
        # zero_cols = set()
        # for row in range(len(matrix)):
        #     for col in range(len(matrix[row])):
        #         if matrix[row][col] == 0:
        #             zero_rows.add(row)
        #             zero_cols.add(col)
        
        # for row in zero_rows:
        #     for col in range(0, len(matrix[row])):
        #         matrix[row][col] = 0
        
        # for col in zero_cols:
        #     for row in range(0, len(matrix)):
        #         matrix[row][col] = 0

        # constant space solution: 
        # handle first row and column separtely to avoid wiping up flags 
        # add row_zero and col_zero flag determine if first row or col must be zeroed
        # this is important because we flag 0 in the first row/col; need to distinguish if the 0 is from original matrix or is it a flag
        row_zero = False
        col_zero = False
        
        # look at first row and col
        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                col_zero = True
                break
        
        for i in range(len(matrix[0])):
            if matrix[0][i] == 0:
                row_zero = True
                break
        
        # set flags
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # handle rows 
        for row in range(1, len(matrix)):
            if matrix[row][0] == 0:
                for col in range(len(matrix[row])):
                    matrix[row][col] = 0
        
        #handle cols
        for col in range(1, len(matrix[0])):
            if matrix[0][col] == 0:
                for row in range(len(matrix)):
                    matrix[row][col] = 0

        #handle first row and first col
        if row_zero:
            for i in range(len(matrix[0])):
                matrix[0][i] = 0
        if col_zero:
            for i in range(len(matrix)):
                matrix[i][0] = 0

            



        