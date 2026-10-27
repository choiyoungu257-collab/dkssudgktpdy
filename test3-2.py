import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt

freq = np.fft.fftfreq(2**14, d= 1.0)
freq[0] = 1

white = np.random.default_rng().normal(size = 2**14)
fourier = np.fft.fft(white)

pink = fourier/(np.abs(freq)**(1/2))
pink = np.fft.ifft(pink)
f, Pxx = signal.welch(pink, fs=1.0)

brown = fourier/(freq)
brown = np.fft.ifft(brown)
f1, Pxx1 = signal.welch(brown, fs=1.0)

fig, axes = plt.subplots(1,2, figsize = (12,4))
axes[0].loglog(f, Pxx)
axes[1].loglog(f1, Pxx1)

valid = f >0
valid1 = f1 >0
slope, intercept = np.polyfit(np.log(f[valid]), np.log(Pxx[valid]), deg =1 )
slope1, intercept1 = np.polyfit(np.log(f1[valid]),np.log(Pxx1[valid]), deg = 1)


y_fit = 10**intercept * (f**slope)
y_fit1 = 10**intercept1 * (f1**slope1)

axes[0].plot(f, y_fit, label = f"Fit: y= {slope:.2f} + {intercept:.2f}")
axes[1].plot(f1, y_fit1, label = f"Fit: y={slope1:.2f}+{intercept1:.2f}")
axes[0].legend()
axes[1].legend()
plt.show()