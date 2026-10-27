#1.0과 1로 이루어진 넘파이 배열을 받는다.
#2. 그걸 p의 확률로 독립적으로 반전
#3. 
import numpy as np

error_rng = np.random.default_rng(seed=30)
my_bits = error_rng.integers(0,2, size = 10**6)
def bsc(bits, p, rng):
    flips = rng.random(len(bits))<p
    return flips

error = bsc(my_bits, 0.01,error_rng)
error_rate = np.sum(error == True)/len(error) *100
print(f"{error_rate}%")

