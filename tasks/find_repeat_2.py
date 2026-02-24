# код с бул листом для проверки использованных элементов, я не знаю какой код работает лучше


def find_repeat(n, l):
    boollist = [False] * n
    for i in range(n):
        if boollist[l[i]]:
            return l[i]
        boollist[l[i]] = True
    return -1