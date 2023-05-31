import numpy as np
import matplotlib.pyplot as plt
dft = []
Wamp = []
Wdb = []
def DFT(x):
    for k in range(0,len(x)):
        z = 0
        for n in range(0,len(x)):
            z += (x[n] * np.exp(-1j*(-2*np.pi * k * n)/len(x)))
        dft.append(z)
    return dft

def widm_amp(wi):
    for k in range(len(wi)):
        Wamp.append((wi[k].real)**2 + (wi[k].imag)**2)
    return Wamp
def widmDB(M):
    for k in range(len(M)):
        Wdb.append(10*np.log10(M[k]))
    return Wdb


fs = 200 # częstotliwość próbkowania
Tc = 1
N = Tc * fs #Liczba próbek
k = np.arange(0,(N/2)-1,1)
fk = k * (fs/N)
DFT(k)
widm_amp(dft)
plt.plot(widmDB(Wamp))
plt.show()