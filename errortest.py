import numpy as np
import matplotlib.pyplot as plt
p=0.3
def flip(n):
    p=0.3
    rng = np.random.default_rng(seed=20)
    num = 2**20
    flips = (rng.random((num,n)) < p).astype(int)
    k = flips.sum(axis=1)
    P = (p**k)*((1-p)**(n-k))
    return P
plt.hist(flip(20),bins=5000)
plt.show()