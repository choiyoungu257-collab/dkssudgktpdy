import numpy as np
from scipy.stats import chisquare
def lcg(seed, a, c, m, n):
    x=seed
    result = []
    for i in range(n):
        x = (a*x+c) %m
        u = x/m
        result.append(u)
    return(np.array(result))
values = lcg(0,1103515245,12345,2**31,10**5)
for i in range(len(values)):
    if values[i] >= 0.5:
        values[i] = 1
    elif values[i] < 0.5:
        values[i] = 0
count_1 = np.sum(values == 1)
count_0 = np.sum(values == 0)

observed = [count_1,count_0]
expected = [len(values)/2, len(values)/2]

chi2_stat, p_value = chisquare(observed, expected)
print(chi2_stat)
print(p_value)
