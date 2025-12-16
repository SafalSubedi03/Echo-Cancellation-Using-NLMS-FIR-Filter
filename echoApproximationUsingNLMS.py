import numpy as np
from signalGeneration import un, dn
import matplotlib.pyplot as plt
import soundfile as sf


def compute_y(w, x, n):
    y = 0
    for k in range(len(w)):
        if n - k >= 0:
            y += w[k] * x[n - k]
    return y

def updatewk(wk, x, n, mu, e, eps=1e-8):
    power = 0
    for k in range(len(wk)):
        if n - k >= 0:
            power += x[n - k] ** 2

    for k in range(len(wk)):
        if n - k >= 0:
            wk[k] = wk[k] + (mu / (power + eps)) * e * x[n - k]
    return wk

def update_mu(w_old, w_new, x, n, e, mu_min, mu_max, eps=1e-8):
    dev = np.linalg.norm(w_new - w_old) ** 2
    power = 0
    for k in range(len(w_old)):
        if n - k >= 0:
            power += x[n - k] ** 2
    mu = dev * (power / (e**2 + eps))
    if mu < mu_min:
        mu = mu_min
    if mu > mu_max:
        mu = mu_max
    return mu

M = 40
mu_max = 1.0
mu_min = 0.01
Fs = 44100
N = min(len(un), len(dn))

w = np.zeros(M)
y = np.zeros(N)
e = np.zeros(N)
mu = mu_max

for n in range(N):
    y[n] = compute_y(w, un, n)
    e[n] = dn[n] - y[n]
    w_old = w.copy()
    w = updatewk(w, un, n, mu, e[n])
    mu = update_mu(w_old, w, un, n, e[n], mu_min, mu_max)

t = np.arange(N) / Fs
fig,axs = plt.subplots(1,3,figsize=(6,6))
axs[0].plot(t,un)
axs[0].set_xlabel("t")
axs[0].set_ylabel("un")
axs[1].plot(t,y)
axs[1].set_xlabel("t")
axs[1].set_ylabel("yn")
axs[2].plot(t,e)
axs[2].set_xlabel("t")
axs[2].set_ylabel("en")

sf.write("error.wav",e,Fs)
sf.write("yn.wav",y,Fs)
print("Files created successfully ")
plt.tight_layout()
plt.show()
