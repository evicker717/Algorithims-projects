def mylarsJourney(grid):
    N = len(grid)
    
    # Initialize tbl array
    tbl = [[0] * N for _ in range(N)]
    
    # Set values for the last row
    for i in range(N):
        tbl[N-1][i] = grid[N-1][i]
    
    # Calculate minimum fuel cost for each cell
    for i in range(N-2, -1, -1):
        for j in range(N):
            tbl[i][j] = grid[i][j] + min(tbl[i+1][j], tbl[i+1][(j-1+N)%N], tbl[i+1][(j+1) % N])
    
    # Find minimum fuel cost in the first row
    ans = tbl[0][0]
    for i in range(1, N):
        ans = min(ans, tbl[0][i])
    
    return ans
grid = [
    [2, 2, 1, 2, 2],
    [2, 1, 2, 2, 2],
    [2, 1, 2, 2, 2],
    [1, 2, 2, 2, 2],
    [2, 2, 2, 2, 1]
]

print("total fuel cost:", mylarsJourney(grid))