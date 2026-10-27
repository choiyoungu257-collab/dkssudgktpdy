import numpy as np
import matplotlib.pyplot as plt
from itertools import product

n = 12
p = 0.1
rates = [1/12, 3/12, 6/12, 9/12]
ks = [int(n*R) for R in rates]

trials = 50
blocks = 200

h2_p = -p * np.log2(p) - (1-p)*np.log2(1-p)
capacity = 1.0 - h2_p

avglist = []

for k, R in zip(ks, rates):
    total_block_errors = 0
    total_block_tested = 0

    all_messages = np.array(list(product([0,1],repeat=k)), dtype=np.uint8)
    num_codewords = len(all_messages)

    for _ in range(trials):
        G = np.random.randint(0,2,size=(k,n),dtype=np.uint8)
        codebook = (all_messages @ G) % 2
        msg_indices = np.random.randint(0, num_codewords, size=blocks)

    for idx in msg_indices:
        tx_codeword = codebook[idx]

        noise = (np.random.rand(n)<p).astype(np.uint8)
        rx_vector = (tx_codeword ^ noise)

        hamming_distances = np.sum(codebook != rx_vector, axis=1)
        min_dist = np.min(hamming_distances)

        closest_indices = np.where(hamming_distances == min_dist)[0]

        decoded_idx = np.random.choice(closest_indices)

        if not np.array_equal(codebook[decoded_idx], tx_codeword) : 
            total_block_errors += 1
    total_block_tested += blocks

    bler = total_block_errors / total_block_tested
    avglist.append(bler)
    print(f"R = {k:2d}/12 ({R:.4f}) | BLER = {bler:.4f}")

plt.figure(figsize=(8,5))
plt.plot(rates, avglist, marker='o', color='b', linewidth=1.8, label='Random Linear Code (n=12)')
plt.axvline(x=capacity, color='red', linestyle='--', linewidth=1.5, label=f'Capacity C(0.1) ≈ {capacity:.3f}')

# 각 데이터 포인트 수치 표기
for r, bler in zip(rates, avglist):
    plt.annotate(f"{bler:.3f}", 
                 xy=(r, bler), 
                 xytext=(r, bler + 0.03),
                 ha='center', fontsize=9, fontweight='bold')

plt.title('Block Error Rate vs Code Rate (n=12, p=0.1)', fontsize=12, pad=12)
plt.xlabel('Code Rate (R = k/n)', fontsize=11)
plt.ylabel('Block Error Rate (BLER)', fontsize=11)
plt.ylim(-0.05, 1.05)
plt.xlim(0, 0.9)
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend(loc='lower right', framealpha=0.9)
plt.tight_layout()
plt.show()

