class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # 8 directions, follow procedure order to update 
        # boundaries: 
        # traversal_states = {
        #     'FIRST_ROW': [(0, -1), (0, 1), (1, 0), (1, -1), (1, 1)],
        #     'FIRST_COL': [(-1, 0), (-1, 1), (0, 1), (1, 0), (1, 1)],
        #     'LAST_ROW' : [(0, -1), (0, 1), (-1, 0), (-1, -1), (-1, 1)],
        #     'LAST_COL' : [(-1, -1), (-1, 0), (0, -1), (1, -1), (1, 0)],
        #     'TOP__LEFT_CORNER' : [(0, 1), (1, 0), (1, 1)],
        #     'TOP_RIGHT_CORNER' : [(0, -1), (1, -1), (1, 0)],
        #     'BOT_LEFT_CORNER': [(-1, 0), (-1, 1), (0, 1)],
        #     'BOT_RIGHT_CORNER': [(0, -1), (0, -1), (-1, 0)],
        #     'MIDDLE' : [(-1, 0), (-1, 1), (-1, 1), (0, 1), (0, -1), (1, 1), (1, -1), (1, 0)]
        # }
        # row = len(board)
        # col = len(board[0])
        # og_board = [row[:] for row in board]
        # traverse_directions = []
        # for i in range(row):
        #     for j in range(col):
        #         # determine which state 
        #         if i == 0 and j == 0:
        #             traverse_directions = traversal_states['TOP__LEFT_CORNER']
        #             #print("TOP_LEFT_CORNER")
        #         elif i == row - 1 and j == 0:
        #             traverse_directions = traversal_states['BOT_LEFT_CORNER']
        #             #print("BOT_LEFT_CORNER")
        #         elif i == 0 and j == col -1:
        #             traverse_directions = traversal_states['TOP_RIGHT_CORNER']
        #             #print("TOP_RIGHT_CORNER")
        #         elif i == row - 1 and j == col -1:
        #             traverse_directions = traversal_states['BOT_RIGHT_CORNER']
        #             #print("BOT_RIGHT_CORNER")
        #         elif i == 0 and j != 0:
        #             traverse_directions = traversal_states['FIRST_ROW']
        #             #print("FIRST_ROW")
        #         elif i == row - 1 and j != 0:
        #             traverse_directions = traversal_states['LAST_ROW']
        #             #print("LAST_ROW")
        #         elif i != 0 and j == 0:
        #             traverse_directions = traversal_states['FIRST_COL']
        #             #print("FIRST_COL")
        #         elif i != 0 and j == col -1:
        #             traverse_directions = traversal_states['LAST_COL']
        #             #print("LAST_COL")
        #         else:
        #             traverse_directions = traversal_states['MIDDLE']
        #             #print("MIDDLE")
        #         life_count, dead_count = 0, 0 
        #         for dirs in traverse_directions:
        #             if og_board[i + dirs[0]][j + dirs[1]] == 1:
        #                 life_count += 1
        #             else:
        #                 dead_count += 1
        #         #life
        #         print("coordinate: ", i, j)
        #         print("life count: ", life_count, "dead_count: ", dead_count)
        #         if og_board[i][j] == 1:
        #             print("og-board: life")
        #             if life_count < 2 or life_count > 3:
        #                 board[i][j] = 0
        #         # dead
        #         else:
        #             print("og-board: dead")
        #             if life_count == 3:
        #                 board[i][j] = 1

        # can have an easier solution where to just traverse the 8 directions and check boundary
        # without using an orginal copy of the board, have to use 2 bit encoding:
        # 00 -> dead will remain dead
        # 10 -> dead will be alive
        # 01 -> alive will be dead
        # 11 -> alive remain alive 
        # python shift operator >> shifts 1 bit to the right: 11 (3) becomes 01(1), 10(2)-> 01(1), 01(1) -> 00
        row = len(board)
        col = len(board[0])
        og_board = [row[:] for row in board]

        # Directions for all 8 neighbors
        directions = [(-1, -1), (-1, 0), (-1, 1),
                      (0, -1),          (0, 1),
                      (1, -1), (1, 0), (1, 1)]

        for i in range(row):
            for j in range(col):
                # Count living neighbors
                life_count = 0
                for dx, dy in directions:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < row and 0 <= nj < col and og_board[ni][nj] == 1:
                        life_count += 1
                
                if og_board[i][j] == 1:
                    if life_count < 2 or life_count > 3:
                        board[i][j] = 0
                else:
                    if life_count == 3:
                        board[i][j] = 1





        