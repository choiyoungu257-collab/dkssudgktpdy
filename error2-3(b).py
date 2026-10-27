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
    h=(-p*np.log2(p)-(1-p)*np.log2(1-p))
    low = 2**(-n*(h+0.05))
    high = 2**(-n*(h-0.05))
    mask = (P>=low) & (P<=high) #(h-e) < -1/n*log2(P) < (h+e) ->> n이 커지면 많은 수열들이 그 확률에 따른 엔트로피에 가까워지고 그 구간의 값들이 대부분을 차지한다.
    select = P[mask]
    return select
print(len(flip(20)))
print(flip(20))
print(2**(20*(-p*np.log2(p)-(1-p)*np.log2(1-p))))
print(2**20)

