import numpy as np
def lcg(seed, a, c, m, n):
    x=seed
    result = []
    for i in range(n):
        x = (a*x+c) %m
        u = x/m
        result.append(u)
    return(np.array(result))

rng = np.random.default_rng()
values = rng.random(10**5)
value1 = lcg(0,5,1,2**8,10**5)
value2 = lcg(0,1103515245,12345,2**31,10**5)
mom = []
son = []
for i in range(len(value2)-1):
    a = (value2[i]-np.mean(value2))*(value2[i+1]-np.mean(value2))
    son.append(a)
    b = (value2[i]-np.mean(value2))**2
    mom.append(b)
rho1 = np.sum(son)/np.sum(mom)
print(rho1)