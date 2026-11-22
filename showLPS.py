ra_ug = [0, 2.25, 4.5, 9, 22.5, 45, 90, 180]
re_ug = [0, 2.5, 5.0, 10, 25, 50, 100, 200]
vol_L = 500e-6 # 500 uL
mw_ra = 4145
mw_re = 2237

ra_uM = [round((ug * 1e-6 / mw_ra) / vol_L * 1e6, 2) for ug in ra_ug]
re_uM = [round((ug * 1e-6 / mw_re) / vol_L * 1e6, 2) for ug in re_ug]

print("Ra-LPS uM:", ra_uM)
print("Re-LPS uM:", re_uM)

import matplotlib.pyplot as plt

plt.plot(ra_uM, ra_ug, marker="o", label="Ra-LPS")
plt.plot(re_uM, re_ug, marker="o", label="Re-LPS")
plt.xlabel("Concentration (µM)")
plt.ylabel("Amount (µg)")
plt.title("Ra-LPS and Re-LPS Concentration Series")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
