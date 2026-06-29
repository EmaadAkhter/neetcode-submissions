class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row=len(grid)
        col=len(grid[0])
        vist=set()
        island=0
        
        def dfs(r,c,f):
            if ((r,c) in vist or
                r<0 or c<0 or
                r>=row or c>=col):
                return 0
            
            if f==1 and grid[r][c]=="1":
                vist.add((r,c))

            if grid[r][c]=="1":
                dfs(r,c,1)
                dfs(r-1,c,1)
                dfs(r+1,c,1)
                dfs(r,c-1,1)
                dfs(r,c+1,1)
                return 1
            
            else:
                return 0
        for r in range(row):
            for c in range(col):
                island+=dfs(r,c,0)
            
        
        return island