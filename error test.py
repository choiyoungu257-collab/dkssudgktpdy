import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import binom

# 1. 파라미터 설정
p = 0.1
n_vals = np.arange(1, 100)  # n=100만 되어도 비트 수는 201개
N_vals = 2 * n_vals + 1  # 3, 5, 7, ..., 201 비트

# 2. 다수결 실패 확률 이론값 계산 (에러 비트 수 >= n + 1)
# binom.sf(k, N, p) = P(X > k)
error_rates = binom.sf(n_vals, N_vals, p)

# 3. 로그-로그 플롯 (끊김 없이 깊은 영역까지 출력)
plt.figure(figsize=(8, 5))
plt.loglog(
    N_vals,
    error_rates,
    "o-",
    color="tab:blue",
    markersize=3,
    label=f"Theory ($p={p}$)",
)

plt.xlabel("Total Block Length ($N = 2n+1$)")
plt.ylabel("Logical Error Rate")
plt.title("Repetition Code: Error Rate vs Block Length")
plt.grid(True, which="both", ls="--", alpha=0.5)

# Y축의 범위를 원하는 극소값(예: 10^-50)까지 명시적으로 지정 가능
# plt.ylim(1e-50, 1)

plt.legend()
plt.tight_layout()
plt.show()