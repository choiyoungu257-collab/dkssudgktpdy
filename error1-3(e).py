import numpy as np
import matplotlib.pyplot as plt
from math import comb
rep_err = 0
p_values = np.linspace(0.001,0.5,200)
hamming = 1-((1-p_values)**7 + 7*p_values*(1-p_values)**6)
for k in range(4,8):
    rep_err = rep_err + (comb(7,k)*p_values**k * (1-p_values)**(7-k))

plt.semilogy(p_values, hamming, label="Hamming(7,4)")
plt.semilogy(p_values, rep_err, label="Repetition")
plt.legend()
plt.show()