def solution(l):
    list_2 = l[:]
    while True:
        sum_ = sum(l)
        if not sum_%3:
            break
        if len(l) == 0:
            return 0
        if len(list_2) == 0:
            l.pop(l.index(min(l)))
            list_2 = l[:]
        if len(list_2) ==0:
            return 0
        if not (sum_ - min(list_2)) % 3:
            l.pop(l.index(min(list_2)))
            list_2 = l[:]

        else:
            list_2.pop(list_2.index(min(list_2)))

    return int("".join([str(i) for i in sorted(l, reverse=True)]))


print (solution([2,3,5,9,9]))

