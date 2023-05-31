import numpy as np
import matplotlib.pyplot as plt
# Zad 1
A=1
f=1
fs=10000 # częstotliwość próbkowania
Tc=1
N= Tc * fs
t=np.linspace(0,Tc,N)
x = (np.e**(-t)*np.sin(np.pi*f*t))/(2.0001+np.cos(np.pi*t))
plt.plot(t,x)
plt.show()