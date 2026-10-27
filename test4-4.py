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

n_sig = sigma**2 * np.ones(N)

sf = np.abs(np.fft.fft(s_sig))
hf = sf/(n_sig+sf)

X = np.fft.fft(x)
X_show = np.fft.ifft(hf * X).real


freq, Pxx = welch(X_show, N, nperseg = 1024)


mse_raw = np.mean((X_show-s_sig)**2) #0.00003144
print(mse_raw)
plt.loglog(freq,Pxx)
plt.show()