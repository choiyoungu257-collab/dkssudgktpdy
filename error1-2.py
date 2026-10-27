import numpy as np
hi = 0
hi1 = np.zeros(3)
error_rng = np.random.default_rng(seed=30)
def bsc(bits, p, rng):
    vote = []
    for i in range(10**5):
        
        flips = rng.random(len(bits))<p
        if np.sum(flips == False) > 1:
            vote.append(0)
        else:
            vote.append(1)
    vote = np.array(vote)
    return vote.sum(0)/len(vote)*100

error1 = bsc(hi1, 0.01 ,error_rng)
error2 = bsc(hi1, 0.05 ,error_rng)
error3 = bsc(hi1, 0.1 ,error_rng)
error4 = bsc(hi1, 0.2 ,error_rng)
error5 = bsc(hi1, 0.5 ,error_rng)
print(f"{error1:.3f},{error2:.3f},{error3:.3f},{error4:.3f},{error5:.3f}")