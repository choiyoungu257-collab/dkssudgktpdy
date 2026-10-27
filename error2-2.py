import numpy as np
import matplotlib.pyplot as plt
p = np.linspace(0,1,100)
h = -p*np.log2(p)-(1-p)*np.log2(1-p)
c = 1-h # 왜 대칭인가, 왜 0.5일때 0인가 ->> h가 왜 대칭이고 0.5일때 1인가 ->그건... h가 0.5기준 우함수이고 1/2일때 log2가 1이 되니까

plt.plot(p,c)
plt.axhline(y=4/7, color='r', linestyle='-')
plt.axhline(y=1/7, color='r', linestyle='-')
plt.axvline(x=0.1, color='b',linestyle='--')
plt.legend()
plt.show()
#0.1일때 4/7은 더 큼, 1/7은 더 작음 ->> shannon's theorem: rate가 채널용량 C보다 크면 에러율을 0으로 만드는 것이 불가능하다.
#같은 rate이어도 더 좋은 코드를 쓰면 오류를 0에 가깝게 만들 수 있고 그 코드는 반드시 존재한다.