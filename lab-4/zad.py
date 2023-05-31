import numpy as np
import matplotlib.pyplot as plt
st = "Michal"
# ord () zwraca l. calkowita reprezentujaca znak unicode
ac = str((''.join(format(ord(i),'b') for i in st))).replace(' ','')

asc = []
for i in str(ac):
    ac = int(i)
    asc.append(ac)

W = 2
Tb = 1 # czas trwania bitu
fn = W * (Tb**(-1))
A1 = 1
A2 = 2
fn1 = (W + 1) / Tb
fn2 = (W + 2) / Tb
rozmiarASC = np.size(asc)
Tc = Tb * rozmiarASC #czas trwania sygnalu
fs = 50
N = Tc * fs #ilosc probek
Ts = 1/fs #okres probkowania
t = np.linspace(0, Tc, N)
# print(rozmiarASC)
# print(np.size(t))
# print(np.size(t)/rozmiarASC)
b = []
p = np.size(t)/rozmiarASC
for i in range(rozmiarASC):
    for j in range(int(p)):
        b.append(asc[i])
def za(t):
    za = []
    for i in range(len(b)):
        if b[i] == 0:
            za.append(A1 * np.sin(2 * np.pi * fn * t[i]))
        elif b[i] == 1:
            za.append(A2 * np.sin(2 * np.pi * fn * t[i]))
    return za
def zp(t):
    zp = []
    for i in range(len(b)):
        if b[i] == 0:
            zp.append(np.sin(2 * np.pi * fn * t[i]))
        elif b[i] == 1:
            zp.append(np.sin(2 * np.pi * fn * t[i] + np.pi))
    return zp
def zf(t):
    zf = []
    for i in range(len(b)):
        if b[i] == 0:
            zf.append(np.sin(2 * np.pi * fn1 * t[i]))
        elif b[i] == 1:
            zf.append(np.sin(2 * np.pi * fn2 * t[i]))
    return zf
za = za(t)
zp = zp(t)
zf = zf(t)


plt.plot(za)
plt.title("Modulacja ASK")
plt.show()
plt.plot(zp)
plt.title("Modulacja PSK")
plt.show()
plt.plot(zf)
plt.title("Modulacja FSK")
plt.show()

def widmoAmplitudowe(wid):
    return np.sqrt((wid.real ** 2) + (wid.imag ** 2))

zafft = np.fft.fft(za)
plt.plot(widmoAmplitudowe(zafft))
plt.title("Widmo amplitutdowe ASK")
plt.show()

zpfft = np.fft.fft(zp)
plt.plot(widmoAmplitudowe(zpfft))
plt.title("Widmo amplitutdowe PSK")
plt.show()

zffft = np.fft.fft(zf)
plt.plot(widmoAmplitudowe(zffft))
plt.title("Widmo amplitutdowe FSK")
plt.show()
