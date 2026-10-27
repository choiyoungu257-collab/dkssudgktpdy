import numpy as np
import matplotlib.pyplot as plt

def flip(n):
    p=0.3
    rng = np.random.default_rng(seed=20)
    num = 10**4
    flips = (rng.random((num,n)) < p).astype(int)
    k = flips.sum(axis=1)
    P = (p**k)*((1-p)**(n-k))
    rate = -np.log2(P) / n #그 수열이 나올 확률에 log2를 취한 것이 왜 엔트로피 값을 나타내는 것이 되는지?
    return rate

fig, axes = plt.subplots(2,2, figsize=(10,8))
axes[0,0].hist(flip(10),bins=50)
axes[0,1].hist(flip(50),bins=50)
axes[1,0].hist(flip(200),bins=50)
axes[1,1].hist(flip(1000),bins=50)
for ax in axes.flat:
    ax.axvline(x=0.881,color='r',linestyle='--') #각각의 수열에 대한 불확실성 즉, 엔트로피는 0.881로 수렴하게 된다.
plt.show()