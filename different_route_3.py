obstacleGrid = [
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
#2
def uniquePathsWithObstacles(obstacleGrid):
    target = [[0 for i in range(len(obstacleGrid[0]))] for j in range(len(obstacleGrid))]
    target[0][0] = 1
    for i in range(len(obstacleGrid)):
        for j in range(len(obstacleGrid[0])):
            if i == 0 and j > 0:
                target[i][j] = target[i][j - 1]
                if obstacleGrid[i][j] == 1:
                    target[i][j] = 0
            if j == 0 and i > 0:
                target[i][j] = target[i - 1][j]
                if obstacleGrid[i][j] == 1:
                    target[i][j] = 0
            elif i > 0 and j > 0:
                target[i][j] = target[i][j - 1] + target[i - 1][j]
                if obstacleGrid[i][j] == 1:
                    target[i][j] = 0
    return target[-1][-1]
print(uniquePathsWithObstacles(obstacleGrid))