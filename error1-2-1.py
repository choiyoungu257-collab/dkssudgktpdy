import numpy as np
import matplotlib.pyplot as plt
error_rng = np.random.default_rng(seed=21)
def bsc(bits, p, rng):
    vote = []
    for i in range((10)**6):
        flips = rng.random(len(bits))<p
        if np.sum(flips == False) > len(bits)//2:
            vote.append(0)
        else:
            vote.append(1)
    vote = np.array(vote)
    return vote.sum(0)/len(vote)
PL = []
error_list = np.arange(1,31)
for n in range(30):
    my_bits = np.zeros(2*n+1)
    PL.append(bsc(my_bits,0.1,error_rng))
plt.loglog(error_list,PL)
plt.show()

