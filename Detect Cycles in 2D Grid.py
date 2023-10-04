class Solution(object):
    def containsCycle(self, grid):
        def dfs(row, col, prev_row, prev_col, target, visited):
            
            if row < 0 or row >= m or col < 0 or col >= n or grid[row][col] != target:
                return False
            
            if visited[row][col]:
                return True
            
            visited[row][col] = True
            
            # Try moving to all adjacent cells (up, down, left, right) except the previous cell
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_row, new_col = row + dr, col + dc
              
                if (new_row, new_col) == (prev_row, prev_col):
                    continue
                
                if dfs(new_row, new_col, row, col, target, visited):
                    return True
            
            return False

        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                
                if not visited[i][j]:
                    if dfs(i, j, -1, -1, grid[i][j], visited):
                        return True
        
        return False

