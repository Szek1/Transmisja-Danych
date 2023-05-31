import numpy as np
import matplotlib.pyplot as plt

fs = 8000 # częstotliwość próbkowania
tc = 6.4 # czas trwania sygnału
#ts okres próbkowania
n = tc * fs #sygnał
t = np.arange(0, 6.4, 1/fs)
u = []
for i in t:
    if 0.5 > i and i>=0:
        u.append(0.9 * np.sin(2 * np.pi * i * 8 - (np.pi/3)) + np.log2(np.abs(np.cos(7*(i**2)) + 2.2)))
    if 1.9 > i and i >= 0.5:
        u.append((np.sin(2*np.cos(4*np.pi*i)*np.pi*i))/(2*(i**2)+1))
    if 3.7 > i and i >= 1.9:
        u.append((i-1.9)**2 - np.cos(13*i))
    if 4.9 > i and i >= 3.7:
        u.append(0.5*(i**0.7)*np.sin(8*i))
    if 6.4 > i and i >= 4.9:
        u.append((2+np.sin(18*i)/(3+np.cos(28*i))))
plt.plot(t, u)
plt.show()