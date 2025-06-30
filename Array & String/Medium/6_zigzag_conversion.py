class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # zig zag pattern [1][09] x numRows then [-1][1] for numRows - 2 entries
        # easier to reverse direction at top and bottom
        # don't need 2d array of character as we don't need to keep track of space in between, we have to join them back anyways
        if numRows == 1 or s is None:
            return s

        start_ptr = 0
        zig_zag_list = [""] * numRows
        current_row = 0
        move_down = True
        for char in s:
            zig_zag_list[current_row] += char
            
            if current_row == numRows -1:
                move_down = False
            elif current_row == 0: 
                move_down = True
            
            current_row += 1 if move_down else -1
        
        return "".join(zig_zag_list)