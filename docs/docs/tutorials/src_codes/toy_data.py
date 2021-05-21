import numpy as np
import matplotlib.pyplot as plt

from cmda.data import ecg_apb_sample

data = ecg_apb_sample()

ecg = data["ECG"]
abp = data["ABP"]

fs = 125
t = np.linspace(1, 1 / fs, len(ecg))
print(len(ecg), len(t))

fig, (ax1, ax2) = plt.subplots(2, sharex=True)
ax1.plot(t, ecg)
ax1.set_ylabel("ECG [mV]")
ax2.plot(t, abp, c="red")
ax2.set_ylabel("ABP [mmHg]")
ax2.set_xlabel("Time [seconds]")
plt.show()
