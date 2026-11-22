import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

# 1. Exact X-axis concentrations (uM) for Ra-LPS
# Reaction volume = 500 uL (0.0005 L), MW = 4145 Da
vol_L = 0.0005
ra_mass_ug = np.array([0, 2.25, 4.5, 9.0, 22.5, 45.0, 90.0, 180.0])
ra_conc_uM = ra_mass_ug / (4145 * vol_L)

# 2. Representative normalized Y-axis values (Relative Ra-LPS / dLptE-His ratio)
ra_bound_rel = np.array([0.00, 0.25, 0.43, 0.62, 0.84, 0.94, 0.98, 1.00])


# 3. One-site specific binding model for curve fitting
def binding_curve(x, bmax, kd):
  return (bmax * x) / (kd + x)


popt_ra, _ = curve_fit(binding_curve, ra_conc_uM, ra_bound_rel, p0=[1.0, 5.0])
ra_x_smooth = np.linspace(0, 95, 200)

# 4. Plot the single curve
fig, ax = plt.subplots(figsize=(6, 4.5), dpi=150)

ax.scatter(
    ra_conc_uM, ra_bound_rel, color="black", s=45, zorder=3, label="Data"
)
ax.plot(
    ra_x_smooth,
    binding_curve(ra_x_smooth, *popt_ra),
    color="black",
    linewidth=1.5,
    label="Fit (Kd approx {:.1f} uM)".format(popt_ra[1]),
)

ax.set_title("Ra-LPS Binding to dLptE-His (Fig. 6B)", fontsize=11, fontweight="bold")
ax.set_xlabel("[Ra-LPS] ($\\mu$M)", fontsize=10)
ax.set_ylabel("Relative LPS bound (a.u.)", fontsize=10)
ax.set_xlim(-3, 95)
ax.set_ylim(-0.05, 1.15)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.legend(frameon=False, loc="lower right")

plt.tight_layout()
plt.savefig("fig6B_ra_lps_only.png", dpi=300)
plt.show()
