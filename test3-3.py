import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import poisson

rng = np.random.default_rng()

poisson_data = rng.poisson(5.0, 1000)
time = np.arange(len(poisson_data))
plt.plot(time, poisson_data)

mean = np.mean(poisson_data)
var = np.var(poisson_data)
plt.axhline(y=mean, color = "green",label=f"mean={mean}")
plt.axhline(y=var, color = "green",label=f"variance={var}")
plt.legend()

plt.show()