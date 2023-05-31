import numpy as np
import matplotlib.pyplot as plt

Tc = 1 # czas trwania sygnału
fm = 100  #częstotliwość sygnału informacyjneogo
fn = 1000
fs = 2 * max(fn,fm) # częstotliwośc próbkowania
N = Tc * fs # ilosc próbek
t = np.linspace(0,Tc,N)
dft = []
def DFT(x):
    for k in range(0,len(x)):
        z = 0
        for n in range(0,len(x)):
            z += (x[n] * np.exp(-1j*(-2*np.pi * k * n)/len(x)))
        dft.append(z)
    return dft
def m(t):
    return np.sin(2 * np.pi * fm * t)
def za(t,ka):
    return (ka * m(t) + 1) * np.cos(2 * np.pi * fn * t)
def zp(t,kp):
    return np.cos(2 * np.pi * fn * t + kp * m(t))
def zf(t,kf):
    return np.cos(2 * np.pi * t + (kf/fm) * m(t))

za1 = za(t,0.5)
za2 = za(t,6)
za3 = za(t,30)
zp1 = zp(t, 0.5)
zp2 = zp(t, (np.pi/2))
zp3 = zp(t, (3 * np.pi))
zf1 = zf(t, 0.5)
zf2 = zf(t, (np.pi/2))
zf3 = zf(t, (3 * np.pi))

# 2 widma
widma = [za1, za2, za3, zp1, zp2, zp3, zf1, zf2, zf3]

def widmoAmplitudowe(wid):
    return np.sqrt((wid.real ** 2) + (wid.imag ** 2))

def widmoDecybelowe(wid):
    return 10 * np.log10(widmoAmplitudowe(wid))

def DB(w,db): #kod wzorowany na kodzie Filipa Urbana, jednak w moim przypadku nie działa poprawnie
    s = widmoDecybelowe(widmoAmplitudowe(w))
    s[np.where(s>0)] = 0
    s[np.where(s < -db)] = 0
    fmin = (s!=0).argmax(axis=0)
    if np.count_nonzero(s) == 0:
        return 0
    fmax = np.max(np.nonzero(s))
    res = fmax-fmin
    return res
print("#### 3dB ####")
for i in widma:
    print(DB(i,3))
print("#### 6dB ####")
for i in widma:
    print(DB(i,6))
print("#### 12dB ####")
for i in widma:
    print(DB(i,12))

for i in widma:
    fft = np.fft.fft(i)
    plt.plot(widmoDecybelowe(widmoAmplitudowe(fft)))
    plt.show()
