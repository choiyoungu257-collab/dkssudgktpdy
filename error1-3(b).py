import numpy as np
from itertools import product


G = np.array([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1],[1,1,0,1],[1,0,1,1],[0,1,1,1]])
H = np.array([[1,1,0,1,1,0,0],[1,0,1,1,0,1,0],[0,1,1,1,0,0,1]])
AN = []
all =list(product([0,1], repeat=4))
min_dist = 7
for b in all:
    b_vector = np.array(b)
    AN.append((G@b_vector)%2)

for i in range(16):
    for j in range(i+1, 16):
        dist = np.sum(AN[i] != AN[j])
        if dist < min_dist:
            min_dist = dist
print(min_dist)


