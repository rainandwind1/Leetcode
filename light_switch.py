def bulbSwitch(n):
    # target = [0 for i in range(n)]
    # for i in range(1,n):
    #     for j in range(n):
    #         if (j + 1) % i == 0:
    #             target[j] = 1 - target[j]

    # target[-1] = 1 - target[-1]
    # return sum(target)
  
    return int(n**0.5)

print(bulbSwitch(3))