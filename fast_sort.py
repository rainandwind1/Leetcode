def fast_sort(target):
    if len(target) < 2:
        return target
    index = int(len(target) /2) - 1
    left = [i for i in target if i < target[index]]
    right = [i for i in target if i > target[index]]
    middle = [i for i in target if i == target[index]]
    return fast_sort(left) + middle + fast_sort(right)
print(fast_sort([12,1,2,3]))