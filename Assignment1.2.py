def myfilter(func, seq):
    result = []
    for i in seq:
        if func(i):
            result.append(i)
    return result


def ispositive(n):
    if (n <= 0):
        return False
    else:
        return True


print(str(myfilter(ispositive, [1, 2, -4, 7, -12])))