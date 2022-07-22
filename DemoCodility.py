def solution(a):
    a.sort()

    if max(a) < 0:
        digit = 1
    if len(a) == 1:
        if a[0] < 1:
            digit = 1
        else:
            digit = a[0] + 1
    else:
        if a[0] > 0:
            for x in range(a[0], a[-1] + 2):
                if x not in a:
                    digit = x
                    break
        else:
            for x in range(1, a[-1] + 2):
                if x not in a:
                    digit = x
                    break
    return digit


print(solution([-5, 1, 3]))
print(solution([30, 50, 100]))
print(solution([0, 6]))
print(solution([90, 98]))
print(solution([1, 2, 3, -1, -2, -8]))
