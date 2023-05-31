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

# Zad 2

y = -t**2 * np.cos(t/0.2) * x
z = x * np.cos(2*np.pi*t**2+np.pi) + 0.276*t**2 * x
v = np.sqrt(np.abs(1.77 - y + z)*np.cos(5.2*np.pi*t)+x+4)
plt.plot(t,y)
plt.show()
plt.plot(t,z)
plt.show()
plt.plot(t,v)
plt.show()

