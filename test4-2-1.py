import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import welch
from scipy.ndimage import gaussian_filter1d

def test(f1,f2,n,N):
    s = np.sin(2*np.pi*f1*n/N)+0.5*np.sin(2*np.pi*f2*n/N)
    return s

N = 2**14 
n = np.arange(N)
s_signal = test(10,200,n, N)**2
total = np.sum(s_signal)/N

def P(SN):
    Pnoise = np.sqrt(total/10**(SN/10))
    return Pnoise

rng = np.random.default_rng()
sigma = P(10)
white = rng.normal(loc=0.0, scale=sigma, size=N)
s_sig = test(10, 200, n, N)

x= s_sig + white 

W_values = np.arange(1, 53, 2)

mse_boxcar_list = []
mse_gaussian_list = []

for W in W_values:
    kernel = np.ones(W)/W
    x_boxcar = np.convolve(x, kernel, mode = "same")
    mse_b = np.mean((s_sig-x_boxcar)**2)
    mse_boxcar_list.append(mse_b)

    sigma = W / 6.0
    x_gaussian = gaussian_filter1d(x, sigma=sigma)
    mse_g = np.mean((s_sig-x_gaussian)**2)
    mse_gaussian_list.append(mse_g)

gaussian = gaussian_filter1d(x, sigma=3.0)

fig, axes = plt.subplots(1, 2, figsize = (12,4))

print(W_values,mse_boxcar_list)
print(W_values, mse_gaussian_list)

axes[0].plot(W_values, mse_boxcar_list)
axes[1].plot(W_values, mse_gaussian_list)
plt.show()