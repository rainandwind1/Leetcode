grid = [[0,2]]

def orangesRotting(grid):
    recurrent = 0
    this_count = 1
    target =[[0 for i in range(len(grid[0]))] for z in range(len(grid)) ]
    while True:
        this_count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if target[i][j]== 0:
                    target[i][j] = grid[i][j]
                if grid[i][j] == 2:
                    if i - 1 >= 0:
                        if grid[i - 1][j] == 1:
                            target[i - 1][j] = 2
                            this_count += 1
                    if i + 1 <= len(grid) - 1:
                        if grid[i + 1][j] == 1:
                            target[i + 1][j] = 2
                            this_count += 1
                    if j - 1 >= 0:
                        if grid[i][j - 1] == 1:
                            target[i][j - 1] = 2
                            this_count += 1
                    if j + 1<= len(grid[i]) - 1:
                        if grid[i][j + 1] == 1:
                            target[i][j + 1] = 2
                            this_count += 1
        grid = target
        target = target =[[0 for i in range(len(grid[0]))] for z in range(len(grid)) ]
        
        if this_count == 0:
            for i in range(len(grid)):
                if 1 in grid[i]:
                    return -1
                if i == len(grid) - 1:
                    return recurrent
        recurrent += 1
    

print(orangesRotting(grid))