import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt

##### funkcje

def koder74(s):
    x1 =(s[0] + s[1] + s[3]) %2
    x2 = (s[0] + s[2] + s[3]) %2
    x4 = (s[1] + s[2] + s[3]) %2
    out  = [x1, x2 , s[0] , x4 , s[1] , s[2],s[3]]
    return out


def dekoder74(s):
    x1 = (s[0] + s[2] + s[4] + s[6]) %2
    x2 = (s[1] + s[2] + s[5] + s[6]) %2
    x4 = (s[3] + s[4] + s[5] + s[6]) %2
    S = (x1 * np.power(2,0)) + (x2 * np.power(2,1)) + (x4 * np.power(2,2))
    if S == 0:
        return [s[2],s[4],s[5],s[6]]
    elif S != 0:
        b = S-1
        if s[b] == 0:
            s[b] = 1
        else:
            s[b] = 0
    return [s[2], s[4], s[5], s[6]]

def modASK(s):
    t = 0
    za = []
    A1 = 1
    A2 = 0.5
    for i in range(len(s)):
        for j in range(200):
            t+= 1/200 # okres między próbkami
            if s[i] == 0:
                za.append(A1 * np.sin(2 * np.pi * t))
            elif s[i] == 1:
                za.append(A2 * np.sin(2 * np.pi * t))
    return za


def modPSK(s):
    zp = []
    t = 0
    for i in range(len(s)):
        for j in range(200):
            t += 1/200
            if s[i] == 0:
                zp.append(np.sin(2 * np.pi * t))
            elif s[i] == 1:
                zp.append(np.sin(2 * np.pi * t + np.pi))
    return zp
def modFSK(s):
    zf = []
    t = 0
    fn1 = 3
    fn2 = 4
    t = 0
    for i in range(len(s)):
        for j in range(200):
            t += 1/200
            if s[i] == 0:
                zf.append(np.sin(2 * np.pi * fn1 * t))
            elif s[i] == 1:
                zf.append(np.sin(2 * np.pi * fn2 * t))
    return zf



def szum(s):
    alfa = 1
    szum = np.random.normal(0,1, size=len(s))
    return s + alfa * szum

def tlumienie(s):
    b = 0.05
    t = 1/200
    for i in range(len(s)):
        s[i] *= np.exp(-b * i * t)
    return s


fn = 2
t = 1/200
#### DEMODULACJA ASK
def demASK(x):
    resInter1 = np.split(x,len(x)/200)
    integral1 = []
    for i in resInter1:
        integral1.append(integrate.trapezoid(i))
    h = np.mean(integral1)
    for i in range(len(integral1)):
        if integral1[i] > h:
            integral1[i] = 1
        elif integral1[i] < h:
            integral1[i] = 0
    return integral1

#### DEMODULACJA PSK
def demPSK(x):
    resInter2 = np.split(x,len(x)/200)
    integral2 = []
    for i in resInter2:
        integral2.append(integrate.trapezoid(i))
    for i in range(len(integral2)):
        if integral2[i] > 0:
            integral2[i] = 1
        elif integral2[i] < 0:
            integral2[i] = 0
    return integral2
### DEMODULACJA FSK
def demFSK(x):
    resInter3 = np.split(x, len(x) / 200)
    integral3 = []
    for i in resInter3:
        integral3.append(integrate.trapezoid(i))
    h = np.mean(integral3)
    for i in range(len(integral3)):
        if integral3[i] < h:
            integral3[i] = 1
        elif integral3[i] > h:
            integral3[i] = 0
    return integral3
#################
### Kodowanie ###
#################
slowo = [1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0]
print("Słowo wejściowe:\n", slowo)
dz = [slowo[i:i + 4] for i in range(0, len(slowo), 4)]
X = []
for i in range(len(dz)):
    zakodowany = koder74(dz[i])
    X += zakodowany
###########
### ASK ###
###########
print("\n ASK \n")
print("Słowo zakodowane:\n", X)
plt.plot(modASK(X))
plt.title("Modulacja ASK")
plt.show()

modASK = modASK(X)
szumASK = szum(modASK)

plt.plot(szumASK)
plt.title("Szum ASK")
plt.show()

tlumASK = tlumienie(szumASK)

plt.plot(tlumASK)
plt.title("Tłumienie ASK")
plt.show()

d = demASK(tlumASK)
d = [d[i:i + 7] for i in range(0, len(d), 7)]
print("Słowo po demodulacji: \n",d)
x = []
for i in range(len(d)):
    zdekodowany = dekoder74(d[i])
    x += zdekodowany
print("Słowo po zdekodowaniu:\n",x)
E = 0
for i in range(len(slowo)):
    if slowo[i] != x[i]:
        E+=1
    BER = E/len(slowo)
print("BER dla ASK = ", BER)
###########
### PSK ###
###########
print("\n PSK \n")
print("Słowo zakodowane:\n", X)
plt.plot(modPSK(X))
plt.title("Modulacja PSK")
plt.show()

modPSK = modPSK(X)
szumPSK = szum(modPSK)

plt.plot(szumPSK)
plt.title("Szum PSK")
plt.show()

tlumPSK = tlumienie(szumPSK)

plt.plot(tlumPSK)
plt.title("Tłumienie PSK")
plt.show()

dm = demPSK(tlumPSK)
d = [dm[i:i + 7] for i in range(0, len(dm), 7)]
print("Słowo po demodulacji: \n",d)
x = []
for i in range(len(d)):
    zdekodowany = dekoder74(d[i])
    x += zdekodowany
print("Słowo po zdekodowaniu:\n",x)
E = 0
BER =0
for i in range(len(slowo)):
    if slowo[i] != x[i]:
        E+=1
    BER = E/len(slowo)
print("BER dla PSK = ",BER)

###########
### FSK ###
###########

print("\n FSK \n")
print("Słowo zakodowane:\n", X)
plt.plot(modFSK(X))
plt.title("Modulacja FSK")
plt.show()

modFSK = modFSK(X)
szumFSK = szum(modFSK)

plt.plot(szumFSK)
plt.title("Szum FSK")
plt.show()

tlumFSK = tlumienie(szumFSK)

plt.plot(tlumFSK)
plt.title("Tłumienie FSK")
plt.show()

dm = demFSK(tlumFSK)
d = [dm[i:i + 7] for i in range(0, len(dm), 7)]
print("Słowo po demodulacji: \n",d)
dekod_msg = []
for i in range(len(d)):
    zdekodowany = dekoder74(d[i])
    dekod_msg += zdekodowany
print("Słowo po zdekodowaniu:\n",dekod_msg)

E = 0
BER = 0
for i in range(len(dz)):
    if slowo[i] != dekod_msg[i]:
        E+=1
    BER = E/len(dz)
print("BER dla FSK = ",BER)
# najlepsze dla PSK