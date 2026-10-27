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

med = np.median(value1)
run = []
for i in range(len(value1)):
    if value1[i] > med:
        run.append("+")
    elif value1[i] < med:
        run.append("-")
    else:
        run.append(0)
run = np.array(run)  
R = 1+ np.sum(run[1:] != run[:-1])

n1 = int(np.sum(run == "+"))
n2 = int(np.sum(run == "-"))
n = n1+n2
E_R = 2*n1*n2/n +1
Var_R = (2*n1*n2*(2*n1*n2-n)) / (n**2 *(n-1))
z = (R-E_R) / np.sqrt(Var_R)
print(f"관측된run수:{R}, 기대값:{E_R:.2f},분산:{Var_R:.2f}, z-score:{z:.4f}")

