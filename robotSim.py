from collections import defaultdict
commands = [4,-1,4,-2,4]
obstacles = [[2,4]]
def robotSim(commands, obstacles):
    row_obstacles = defaultdict(list)
    col_obstacles = defaultdict(list)
    for j in obstacles:
        col_obstacles[j[0]].append(j[1])
        row_obstacles[j[1]].append(j[0])
    robot_point = [0,0]
    index_dir =  0 
    direction = [1,2,3,4]#上右下左
    for i in commands:
        if i <= 9 and i >= 1:
            if direction[index_dir] == 1:
                target = robot_point[1]
                if  not col_obstacles[target]:
                    robot_point[0] += i
                else:
                    for n in range(i):
                        robot_point[0] += 1
                        if robot_point[0] not in col_obstacles[target]:
                            continue
                        else:
                            robot_point[0] -= 1
                            break
            elif direction[index_dir] == 2:
                target = robot_point[0]
                
                if  not row_obstacles[target]:
                    robot_point[1] += i
                else:
                    for n in range(i):
                        robot_point[1] += 1
                        if robot_point[1] not in row_obstacles[target]:
                            continue
                        else:
                            robot_point[1] -= 1
                            break
            elif direction[index_dir] == 4:
                target = robot_point[1]
                if  not row_obstacles[target]:
                    robot_point[1] -= i
                else:
                    for n in range(i):
                        robot_point[1] -= 1
                        if robot_point[1] not in row_obstacles[target]:
                            continue
                        else:
                            robot_point[1] += 1
                            break
            elif direction[index_dir] == 3:
                target = robot_point[1]
                if  not col_obstacles[target]:
                    robot_point[0] -= i
                else:
                    for n in range(i):
                        robot_point[0] -= 1
                        if robot_point[0] not in col_obstacles[target]:
                            continue
                        else:
                            robot_point[0] += 1
                            break
        elif i == -1:
            index_dir += 1
            if index_dir >= 4:
                index_dir = 0
        elif i == -2:
            index_dir -= 1
            if index_dir <= -1:
                index_dir = 3
    return (robot_point[0]**2 + robot_point[1]**2)


print(robotSim(commands,obstacles))

#leetcode 题解代码思路较好
