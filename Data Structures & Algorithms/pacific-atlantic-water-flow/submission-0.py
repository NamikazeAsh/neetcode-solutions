class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        atlantic, pacific = set(),set()

        def dfs(r,c,ocean,prevHeight):
            #breakcase
            if (r,c) in ocean or r<0 or r>=len(heights) or c<0 or c>=len(heights[0]) or heights[r][c]<prevHeight:
                return
            
            #main-exploration
            ocean.add((r,c))
            dfs(r-1,c,ocean,heights[r][c])
            dfs(r+1,c,ocean,heights[r][c])
            dfs(r,c-1,ocean,heights[r][c])
            dfs(r,c+1,ocean,heights[r][c])

        for r in range(len(heights)):
            dfs(r,0,pacific,0) #row, col 1, pacific
            dfs(r,len(heights[0])-1,atlantic,0) #row, last col, atlantic
        
        for c in range(len(heights[0])):
            dfs(0,c,pacific,0) #row 1, col, pacific
            dfs(len(heights)-1,c,atlantic,0) #last row, col, atlantic

        results = []

        #final check loop
        for x in atlantic:
            if x in pacific:
                results.append(x)

        return results