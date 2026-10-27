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

W = 18
kernel = np.ones(W)/W
boxcar = np.convolve(x, kernel, mode="same")

gaussian = gaussian_filter1d(x, sigma=10.0)

fig, axes = plt.subplots(1, 3, figsize = (12,8))

freqs , Pxx = welch(x, fs=N, nperseg = 1024)
freqs1, Pxx1 = welch(boxcar, fs=N, nperseg = 1024)
freqs2, Pxx2 = welch(gaussian, fs=N, nperseg = 1024)

axes[0].loglog(freqs, Pxx)
axes[1].loglog(freqs1, Pxx1)
axes[2].loglog(freqs2, Pxx2)

plt.show()