import numpy as np
import matplotlib.pyplot as plt
Tc = 1 # czas trwania sygnału
fm = 100  #częstotliwość sygnału informacyjneogo
fn = 1000
fs = 2 * max(fn,fm) # częstotliwośc próbkowania
N = Tc * fs # ilosc próbek
t = np.linspace(0,Tc,N)
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