import numpy as np
import matplotlib.pyplot as plt

x = [1,3,5,7]
X = []
def DFT(x):
    for k in range(0,len(x)):
        z = 0
        for n in range(0,len(x)):
            z += (x[n] * np.exp(-1j*(-2*np.pi * k * n)/len(x)))
        X.append(z)
    return X
DFT(x)
print(X)