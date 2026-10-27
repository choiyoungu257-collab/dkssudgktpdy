def lcg(seed, a, c, m, n) :
    x=seed
    result = []
    for i in range(n):
        x = (a*x+c) %m
        u = x/m
        result.append(u)
    return result
print(lcg(0, 1103515245, 12345 ,2**31, 20))