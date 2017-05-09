import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

data_rate = 5 #Gbps
taps = [0.75,-0.25]

taps2 = np.array( [0.75,-0.25])*2

w,h = signal.freqz(taps)

plt.plot(w/np.pi*2.5, 20 * np.log10(abs(h)), 'b',label="de-emphasis")

w,h = signal.freqz(taps2)

plt.plot(w/np.pi*2.5, 20 * np.log10(abs(h)), 'r',label="pre-emphasis")
plt.ylabel('Amplitude [dB]', color='b')
plt.xlabel('Frequency (GHz)')
plt.grid()
plt.legend(loc="best")

plt.show()
