class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        #time complexity:O(m+n)
        #space complexity:o(m+n)+ stack
    
        rows ,cols =len(grid),len(grid[0])
        visit=set()
        #r,c are the current position we are on
        def dfs(r,c):
            #base case
            if (r<0 or r == rows or  c < 0 or c==cols or grid[r][c]==0 or (r,c) in visit):
                return 0

            visit.add((r,c))
            return (1+ dfs(r+1,c)+
                        dfs(r-1,c)+
                        dfs(r,c+1)+
                        dfs(r,c-1))
        area=0
        for r in range(rows):
            for c in range(cols):
                area=max(area,dfs(r,c))
        return area
