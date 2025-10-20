class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        # 3x3 filter, round downt he average of the cell and 8 surrounding cells
        row = len(img)
        col = len(img[0])
        from copy import deepcopy
        new_img = deepcopy(img)
        for r in range(row):
            for c in range(col):
                tot_sum = 0
                num_cell = 0 
                for i in range(3):
                    for j in range(3):
                        nx, ny = r+i, c+j
                        if 0 <= nx <= row - 1 and 0<= ny <= col -1:
                            tot_sum += img[nx][ny]
                            num_cell += 1
                #print(tot_sum, num_cell)
                update = tot_sum // 9
                new_img[r][c] = update
        return new_img
