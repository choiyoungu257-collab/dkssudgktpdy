from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np
def lcg(seed, a, c, m, n):
    x=seed
    result = []
    for i in range(n):
        x = (a*x+c) %m
        u = x/m
        result.append(u)
    return(np.array(result))

values = lcg(0,1103515245,12345,2**31,10**5)
x= values[:-1]
y= values[1:]
z1 = np.sqrt(-2*np.log(x))*np.cos(2*np.pi*y)
z2 = np.sqrt(-2*np.log(x))*np.sin(2*np.pi*y)

x_theory = np.linspace(-4,4, 1000)
y_theory = norm.pdf(x_theory, loc=0, scale =1)


fig, axes = plt.subplots(1, 2, figsize=(12,4))
axes[0].hist(z1,bins = 100,alpha=0.5,density=True)
axes[1].hist(z2, bins = 100,alpha=0.5, density =True)
axes[0].plot(x_theory,y_theory, 'r-', linewidth=2,alpha=0.7)
axes[1].plot(x_theory,y_theory, 'r-',linewidth=2,alpha=0.7)
plt.legend()
plt.show()
