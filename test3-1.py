import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as signal

white = np.random.default_rng().normal(size=2**14)
f, Pxx = signal.welch(white, fs=1.0)

plt.figure(figsize=(8,4))
plt.loglog(f, Pxx)

mean_Pxx = np.mean(Pxx[1:])  
plt.axhline(mean_Pxx, color='r', linestyle='--', label=f'Mean level = {mean_Pxx:.3f}')

plt.xlabel('Frequency')
plt.ylabel('PSD')
plt.legend()
plt.show()
