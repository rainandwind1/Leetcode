moves = "UDUDUUDD"
def judgeCircle(moves):
    target = list(moves)
    level = 0
    vertical = 0
    for i in target:
        if i == 'U':
            vertical += 1
        if i == 'D':
            vertical -= 1
        if i == 'L':
            level += 1
        if i == 'R':
            level -= 1
    if vertical == 0 and level == 0:
        return True
    return False





print(judgeCircle(moves))