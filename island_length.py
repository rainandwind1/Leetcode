island = [[1,0]]
def islandPerimeter(grid):
    len_init = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            count_around = 0
            if grid[i][j] == 0:
                continue
            else:
                if i - 1 >= 0:
                    if grid[i - 1][j] == 1:   # 上
                        count_around += 1
                
                if i + 1 < len(grid):    
                    if grid[i + 1][j] == 1:   #下
                        count_around += 1

                if j - 1 >= 0:
                    if grid[i][j - 1] == 1:   #左
                        count_around += 1
                
                if j + 1 < len(grid[i]):
                    if grid[i][j + 1] == 1:   #右
                        count_around += 1
                len_init += 4 - count_around
    return len_init

print(islandPerimeter(island))