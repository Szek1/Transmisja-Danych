import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
st = "Michal"
# ord () zwraca l. calkowita reprezentujaca znak unicode
ac = str((''.join(format(ord(i),'b') for i in st))).replace(' ','')

asc=[]
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

print(rozmiarASC)
print(np.size(t))
print(np.size(t)/rozmiarASC)

b = []
p = np.size(t)/rozmiarASC
for i in range(rozmiarASC):
    for j in range(int(p)):
        b.append(asc[i])
# print(len(b))
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

sinus = np.sin(2 * np.pi * fn * t)
#### DEMODULACJA ASK
def demASK():
    res1 = za * sinus
    resInter1 = np.split(res1,len(asc))
    integral1 = []
    for i in resInter1:
        integral1.append(integrate.trapezoid(i))

    # plt.plot(integral1)
    # plt.show()
    h=int((np.size(t)/rozmiarASC)/1.3)

    for i in range(len(integral1)):
        if integral1[i] > h:
            integral1[i] = 1
        elif integral1[i] < h:
            integral1[i] = 0
    plt.plot(integral1)
    plt.show()
    print(integral1)

#### DEMODULACJA PSK
def demPSK():
    res2 = zp * sinus
    resInter2 = np.split(res2, len(asc))
    integral2 = []

    for i in resInter2:
        integral2.append(integrate.trapezoid(i))

    plt.plot(integral2)
    plt.show()

    for i in range(len(integral2)):
        if integral2[i] < 0:
            integral2[i] = 1
        elif integral2[i] > 0:
            integral2[i] = 0

    print(integral2)

### DEMODULACJA FSK
def demFSK():
    sinfn1 = np.sin(2 * np.pi * fn1 * t)
    sinfn2 = np.sin(2 * np.pi * fn2 * t)

    res3n = zf * sinfn1
    res3p = zf * sinfn2
    resInter3p = np.split(res3p, len(asc))
    resInter3n = np.split(res3n, len(asc))
    integral3n = []
    integral3p = []

    for i in resInter3p:
        integral3p.append(integrate.trapezoid(i))
    for i in resInter3n:
        integral3n.append(np.negative(integrate.trapezoid(i)))

    sumIntegral = np.add(integral3p,integral3n)
    # plt.plot(sumIntegral)
    # plt.show()
    for i in range(len(sumIntegral)):
        if sumIntegral[i] < 0:
            sumIntegral[i] = 0
        elif sumIntegral[i] > 0:
            sumIntegral[i] = 1
    plt.plot(sumIntegral)
    plt.show()
    print(sumIntegral)
demASK()
demPSK()
demFSK()