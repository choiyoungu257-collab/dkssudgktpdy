import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import welch

# 1. 신호 생성 함수 (Ground Truth)
def test(f1, f2, n, N):
  return np.sin(2 * np.pi * f1 * n / N) + 0.5 * np.sin(2 * np.pi * f2 * n / N)


# 2. 파라미터 및 원본 신호 생성
N = 2**14
n = np.arange(N)
f1, f2 = 10, 200

s = test(f1, f2, n, N)
P_signal = np.mean(s**2)

# 3. SNR 기준 노이즈 표준편차 계산
target_snr = 10.0  # 10 dB
P_noise = P_signal / (10 ** (target_snr / 10.0))
sigma = np.sqrt(P_noise)

# 4. 화이트 가우시안 노이즈 생성 및 합성
rng = np.random.default_rng()
noise = rng.normal(loc=0.0, scale=sigma, size=N)
x = s + noise  # Noisy observation

# 5. Welch PSD 계산 (정규화 주파수 스케일: fs=N으로 두면 주파수 단위가 인덱스 k와 일치함)
freqs, Pxx = welch(x, fs=N, nperseg=1024)

# 6. 서브플롯 시각화 (1행 2열)
fig, axes = plt.subplots(1, 2, figsize=(13, 4.5))

# (1) 시간 영역 Short Trace (앞의 200개 샘플)
axes[0].plot(
    n[:200], x[:200], color="gray", alpha=0.7, label=f"Noisy $x[n]$ ({target_snr} dB)"
)
axes[0].plot(n[:200], s[:200], color="tab:red", lw=2, label="Ground Truth $s[n]$")
axes[0].set_xlabel("Sample Index ($n$)")
axes[0].set_ylabel("Amplitude")
axes[0].set_title("Time Domain (Short Trace)")
axes[0].grid(True, ls="--", alpha=0.5)
axes[0].legend()

# (2) 주파수 영역 (Welch PSD, log-log 스케일)
# 0 Hz 성분 제외하고 플롯
valid_idx = freqs > 0
axes[1].loglog(
    freqs[valid_idx],
    Pxx[valid_idx],
    color="tab:blue",
    lw=1.5,
    label="Welch PSD of $x[n]$",
)
axes[1].axvline(
    x=f1, color="tab:red", linestyle="--", alpha=0.8, label=f"$f_1 = {f1}$"
)
axes[1].axvline(
    x=f2, color="tab:green", linestyle="--", alpha=0.8, label=f"$f_2 = {f2}$"
)

axes[1].set_xlabel("Frequency Index ($k$) [log scale]")
axes[1].set_ylabel("PSD [log scale]")
axes[1].set_title("Frequency Domain (Well-separated Peaks + Noise Floor)")
axes[1].grid(True, which="both", ls="--", alpha=0.5)
axes[1].legend()

plt.tight_layout()
plt.show()