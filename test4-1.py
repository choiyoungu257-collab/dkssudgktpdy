import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import welch

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

freqs , Pxx = welch(x, fs=N, nperseg = 1024)
freqs1, Pxx1 = welch(s_sig, fs=N, nperseg= 1024)
fig, axes = plt.subplots(1, 2, figsize = (12,4))
axes[0].loglog(freqs, Pxx)
axes[1].loglog(freqs1, Pxx1)
plt.show()