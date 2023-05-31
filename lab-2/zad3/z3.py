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


fs = 800 # częstotliwość próbkowania
Tc = 1
N = Tc * fs #Liczba próbek
# k = np.arange(0,(N/2)-1,1)
# fk = k * (fs/N)
### 3
f=1
t=np.linspace(0,Tc,N)
z1 = (np.e**(-t)*np.sin(np.pi*f*t))/(2.0001+np.cos(np.pi*t))
# DFT(z1)
# print(dft)
# plt.plot(widm_amp(dft))
# plt.show()

# y = -t**2 * np.cos(t/0.2) * z1
# z = z1 * np.cos(2*np.pi*t**2+np.pi) + 0.276*t**2 * z1
# v = np.sqrt(np.abs(1.77 - y + z)*np.cos(5.2*np.pi*t)+z1+4)
#y
# DFT(y)
# print(dft)
# plt.plot(widm_amp(dft))
# plt.show()
#z
# DFT(z)
# print(dft)
# plt.plot(widm_amp(dft))
# plt.show()
#v
# DFT(v)
# print(dft)
# plt.plot(widm_amp(dft))
# plt.show()

#### Z3
# fs = 800 # częstotliwość próbkowania
# tc = 6.4 # czas trwania sygnału
# #ts okres próbkowania
# n = tc * fs #sygnał
# t = np.arange(0, 6.4, 1/fs)
# u = []
# for i in t:
#     if 0.5 > i and i>=0:
#         u.append(0.9 * np.sin(2 * np.pi * i * 8 - (np.pi/3)) + np.log2(np.abs(np.cos(7*(i**2)) + 2.2)))
#     if 1.9 > i and i >= 0.5:
#         u.append((np.sin(2*np.cos(4*np.pi*i)*np.pi*i))/(2*(i**2)+1))
#     if 3.7 > i and i >= 1.9:
#         u.append((i-1.9)**2 - np.cos(13*i))
#     if 4.9 > i and i >= 3.7:
#         u.append(0.5*(i**0.7)*np.sin(8*i))
#     if 6.4 > i and i >= 4.9:
#         u.append((2+np.sin(18*i)/(3+np.cos(28*i))))
# DFT(u)
# print(dft)
# plt.plot(widm_amp(dft))
# plt.show()

###z4
fs = 22050
Tc = 1
N = Tc * fs
t=np.linspace(0,Tc,N)
# b1=0
# for h in range(1,3):
#     b1+=(np.sin(6 * np.pi * t * (h ** 2)))/(((2 * h + 1) ** 2) + np.sin(12 * np.pi * t))
# DFT(b1)
# print(dft)
# plt.plot(widm_amp(dft))
# plt.show()

# b2=0
# for h in range(1,7):
#     b2+=(np.sin(6 * np.pi * t * (h ** 2)))/(((2 * h + 1) ** 2) + np.sin(12 * np.pi * t))
# DFT(b2)
# print(dft)
# plt.plot(widm_amp(dft))
# plt.show()

# b3=0
# for h in range(1,27):
#     b3+=(np.sin(6 * np.pi * t * (h ** 2)))/(((2 * h + 1) ** 2) + np.sin(12 * np.pi * t))
# DFT(b3)
# print(dft)
# plt.plot(widm_amp(dft))
# plt.show()