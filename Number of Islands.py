class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        
        #to get the length of rows and columns
        rows,cols=len(grid),len(grid[0])

        visited= set()
        island=0

        def bfs(r,c):
            q=collections.deque()
            visited.add((r,c))
            q.append((r,c))

            while q:
                row,col = q.popleft()
                #to check the adjecent position of the one poped
                directions=[[1,0],[-1,0],[0,1],[0,-1]]
                for dr ,dc in directions:
                    r=row+dr
                    c=col + dc
                    if (r in range (rows) and 
                        c in range (cols) and
                        grid[r][c]=="1"and
                        (r,c)not in visited):
                        q.append((r,c))
                        visited.add((r,c))


        for r in range (rows):
            for c in range(cols):
                #to traverse it and mark it visited
                if grid[r][c]=='1' and (r,c) not in visited:
                    bfs(r,c)
                    island+=1
        return island
