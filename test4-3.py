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
fourier = np.fft.fft(x) #주파수별 진폭값
fourier[600:N-600] = 0
x_cut = np.fft.ifft(fourier) #시간별 진폭값

#fourier[250 : N - 250] = 0
#x_cut = np.fft.ifft(fourier).real

x_gaussian = gaussian_filter1d(x, sigma = 3.0)

mse_raw = np.mean((s_sig-x)**2)
mse_gaussian = np.mean((s_sig-x_gaussian)**2)
print(mse_gaussian) # 0.005583082971999102
#mse_boxcar에선 최저가 (0.0038260506686101127)
#mse_gaussian에선 최저가 0.0037160856464518153

freq, Pxx = welch(x_cut, fs=N, nperseg=1024)
plt.loglog(freq, Pxx)
plt.show()
#유한한기저