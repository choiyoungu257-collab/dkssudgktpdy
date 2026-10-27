import numpy as np
import matplotlib.pyplot as plt
p = np.linspace(0,1,100)
h = -p*np.log2(p)-(1-p)*np.log2(1-p) #베르누이 확률변수 하나의 이론적 엔트로피 -> 엔트로피 : 확률변수의 불확실성
plt.plot(p,h)
print(-0.3*np.log2(0.3)-(0.7)*np.log2(0.7))
plt.show()