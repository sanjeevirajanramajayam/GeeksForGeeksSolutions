class Solution:
    def cntOnes(self, grid):
        # code here
        visited = [[0 for i in range(len(grid[0]))] for i in range(len(grid))]
        ROWS = len(grid)
        COLS = len(grid[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        cnt = 0
        ans = sum([sum(x) for x in grid])
        def dfs(i, j):
            nonlocal cnt
            # print(i, j)
            if visited[i][j] == 1:
                return
            else:
                visited[i][j] = 1
                cnt += 1
            for nr, nc in directions:
                nrow = i + nr
                ncol = j + nc
                if nrow >= 0 and nrow < ROWS and ncol >= 0 and ncol < COLS:
                    if grid[nrow][ncol] == 1:
                        dfs(nrow, ncol)
                        visited[nrow][ncol] = 1
        for i in range(len(grid[0])):
            if grid[0][i] == 1:
                dfs(0, i)
            if grid[len(grid) - 1][i] == 1:
                dfs(len(grid) - 1, i)

        for i in range(len(grid)):
            if grid[i][0] == 1:
                dfs(i, 0)
            if grid[i][len(grid[0]) - 1] == 1:
                dfs(i, len(grid[0]) - 1)
        
        # print(visited)
        return ans - cnt
        