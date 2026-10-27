"""
Griffiths 5.22 — Dirac comb (periodic delta-function potential) band structure.

Equation 5.71 (with m = hbar = a = 1):

    cos(q) = f(E) = cos(k) + (alpha / k) * sin(k),      k = sqrt(2E)

For a given E, an allowed (propagating) state exists only when |f(E)| <= 1.
Then  q = +/- arccos(f(E)),  which gives the two branches of E(q).
"""

import numpy as np
import matplotlib.pyplot as plt

# ----------------------------------------------------------------------
# parameters
# ----------------------------------------------------------------------
ALPHA = 1.0          # delta-function strength
E_MAX = 30.0         # top of the energy window
N_E = 30_000         # number of energy samples


def f(E, alpha=ALPHA):
    """Right-hand side of Eq. 5.71.  Handles the k -> 0 limit via sinc."""
    k = np.sqrt(2.0 * E)
    # sin(k)/k -> 1 as k -> 0 ; np.sinc(x) = sin(pi x)/(pi x)
    return np.cos(k) + alpha * np.sinc(k / np.pi)


# ----------------------------------------------------------------------
# scan the energy axis and keep the allowed values
# ----------------------------------------------------------------------
E = np.linspace(0.0, E_MAX, N_E)
rhs = f(E)

allowed = np.abs(rhs) <= 1.0
E_ok = E[allowed]
q_ok = np.arccos(rhs[allowed])          # principal branch, 0 <= q <= pi


def band_edges(E, allowed):
    """Return [(E_bottom, E_top), ...] for each contiguous allowed region."""
    idx = np.flatnonzero(allowed)
    if idx.size == 0:
        return []
    breaks = np.flatnonzero(np.diff(idx) > 1)
    groups = np.split(idx, breaks + 1)
    return [(E[g[0]], E[g[-1]]) for g in groups]


bands = band_edges(E, allowed)

print(f"alpha = {ALPHA},  0 <= E <= {E_MAX}")
print(f"{'band':>4}  {'E_bottom':>10}  {'E_top':>10}  {'width':>8}   "
      f"{'(j*pi)^2/2':>10}")
for j, (lo, hi) in enumerate(bands, start=1):
    print(f"{j:>4}  {lo:10.4f}  {hi:10.4f}  {hi - lo:8.4f}   "
          f"{(j * np.pi) ** 2 / 2:10.4f}")

# ----------------------------------------------------------------------
# plot
# ----------------------------------------------------------------------
fig, (ax1, ax2) = plt.subplots(
    1, 2, figsize=(12, 6), gridspec_kw={"width_ratios": [2, 1]}
)

# --- left panel: E(q), both +q and -q branches ------------------------
for lo, hi in bands:
    m = (E_ok >= lo) & (E_ok <= hi)
    ax1.plot(q_ok[m], E_ok[m], color="#1f4e79", lw=1.8)
    ax1.plot(-q_ok[m], E_ok[m], color="#1f4e79", lw=1.8)
    ax1.axhspan(lo, hi, color="#1f4e79", alpha=0.07, lw=0)

# band tops sit exactly at the infinite-square-well levels (Problem 5.21b)
for j in range(1, 10):
    Ej = (j * np.pi) ** 2 / 2
    if Ej <= E_MAX:
        ax1.axhline(Ej, color="#c0392b", ls=":", lw=1, zorder=0)

ax1.set_xlabel(r"$qa$")
ax1.set_ylabel(r"$E$   $(\hbar^2/ma^2)$")
ax1.set_title(rf"Band structure of the Dirac comb ($\alpha={ALPHA:g}$)")
ax1.set_xlim(-np.pi, np.pi)
ax1.set_ylim(0, E_MAX)
ax1.set_xticks([-np.pi, -np.pi / 2, 0, np.pi / 2, np.pi])
ax1.set_xticklabels([r"$-\pi$", r"$-\pi/2$", "0", r"$\pi/2$", r"$\pi$"])
ax1.grid(alpha=0.25)

# --- right panel: f(E) with the |f| <= 1 window ------------------------
ax2.plot(rhs, E, color="#444444", lw=1.2)
ax2.axvspan(-1, 1, color="#1f4e79", alpha=0.12, lw=0)
ax2.axvline(-1, color="#1f4e79", lw=1)
ax2.axvline(1, color="#1f4e79", lw=1)
ax2.set_xlabel(r"$f(E)=\cos k+\frac{\alpha}{k}\sin k$")
ax2.set_title(r"allowed when $|f|\leq 1$")
ax2.set_xlim(-4, 4)
ax2.set_ylim(0, E_MAX)
ax2.grid(alpha=0.25)

fig.tight_layout()
fig.savefig("/mnt/user-data/outputs/band_structure.png", dpi=150)
print("\nsaved -> band_structure.png")