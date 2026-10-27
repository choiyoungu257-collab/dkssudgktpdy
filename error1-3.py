import numpy as np
from itertools import product


G = np.array([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1],[1,1,0,1],[1,0,1,1],[0,1,1,1]])
H = np.array([[1,1,0,1,1,0,0],[1,0,1,1,0,1,0],[0,1,1,1,0,0,1]])
AN = []
all =list(product([0,1], repeat=4))

for b in all:
    b_vec = np.array(b)
    AN.append((G @ b_vec)%2)
print(AN)
    