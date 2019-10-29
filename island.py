grid_ = [[1,1,1,0,0],
[1,0,1,0,0],
[1,1,1,1,0],
[0,1,1,0,0],
[0,0,0,0,1]]
#print(grid)
def resolve_island(grid):
    count_island = 0
    count_island = 0
    count_memory = 5
    times = 0
    while True:
        times += 1
        if count_memory == 0:
            break
        count_memory = 0
        print(grid)
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                count_around = 0
                if grid[i][j] == 0:
                    continue

                if i - 1 >= 0:
                    if grid[i - 1][j] == 1:   # 上
                        count_around += 1
                
                if i + 1 < len(grid[i]):    
                    if grid[i + 1][j] == 1:   #下
                        count_around += 1

                if j - 1 >= 0:
                    if grid[i][j - 1] == 1:   #左
                        count_around += 1
                
                if j + 1 < len(grid[i]):
                    if grid[i][j + 1] == 1:   #右
                        count_around += 1

                #判断周围岛屿数量，如果大于2则说明其可以赋值为零，如果为零则表示为孤岛，孤岛数量加一
                if count_around  == 1:
                    grid[i][j] = 0
                count_memory += count_around
        print("number",times,grid,"\n")
    for i in range(len(grid)):
        count_island += sum(grid[i])
    return count_island
print(resolve_island(grid_))