class Solution:
    def minMoves(self, matrix: List[str]) -> int:
        # 0-1 edge weights, dijstra problem
        # preprocess portal letters, need a distance array to track shortest distance
        from collections import defaultdict, deque

        row = len(matrix)
        col = len(matrix[0])

        teleport = defaultdict(list)
        for i in range(row):
            for j in range(col):
                if 'A' <= matrix[i][j] <= 'Z':
                    teleport[matrix[i][j]].append((i,j))
        
        dist = [[float('inf') for j in range(col)] for i in range(row)]
        dist[0][0] = 0
        queue = deque()
        dirs = [(0,1), (0, -1), (-1,0), (1,0)]
        used_teleport = set() 
        queue.append( (0,0))

        while queue:
            r, c = queue.popleft()
            cur_d = dist[r][c]

            if r == row -1 and c == col - 1:
                return cur_d
            
            # teleport, each portal used once
            if 'A' <= matrix[r][c] <= 'Z' and matrix[r][c] not in used_teleport:
                for nx, ny in teleport[matrix[r][c]]:
                    if cur_d < dist[nx][ny]:
                        dist[nx][ny] = cur_d
                        queue.appendleft((nx,ny)) #process 0-cost nodes first
                used_teleport.add(matrix[r][c])
            
            #print(r,c,cur_d)
            for dx, dy in dirs:
                nx, ny = r+dx, c+dy
                #print("options:", nx, ny)
                if nx in range(row) and ny in range(col) and cur_d + 1 < dist[nx][ny] and matrix[nx][ny] != '#':
                    dist[nx][ny] = cur_d+1
                    queue.append((nx,ny)) 
                    #print("next move: ", nx, ny, cur_d + 1)
        
        return -1
        

        
