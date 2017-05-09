import numpy as np
import matplotlib.pyplot as plt


pattern = [-1,-1,-1,-1,-1,1,1,1,1,1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1]
taps_pre = [-0.25,0.75] 
taps_post = [0.75,-0.25]

sa_per_ui = 10

wave_orig = np.repeat(pattern,sa_per_ui)

wave_pre = np.zeros((len(pattern)+len(taps_pre)-1)*sa_per_ui)
for i in range(sa_per_ui):
    wave_pre[i::sa_per_ui] = np.convolve(wave_orig[::sa_per_ui],taps_pre)

wave_post = np.zeros((len(pattern)+len(taps_post)-1)*sa_per_ui)
for i in range(sa_per_ui):
    wave_post[i::sa_per_ui] = np.convolve(wave_orig[::sa_per_ui],taps_post)


plt.subplot(311)
plt.plot(wave_orig,label="orginal")
plt.ylim([-1.2,1.2])
plt.legend()
plt.subplot(312)
plt.plot(wave_pre,label="pre cursor\ntaps=[-0.25,0.75]")
plt.ylim([-1.2,1.2])
plt.legend()
plt.subplot(313)
plt.plot(wave_post,label="post cursor\ntaps=[0.75,-0.25]")
plt.ylim([-1.2,1.2])
plt.legend()
plt.show()
