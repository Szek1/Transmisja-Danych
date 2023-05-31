import numpy as np

def hamming1511(s):
    I = np.eye(11)
    P = np.array([
        [0,0,1,1],
        [0,1,0,1],
        [0,1,1,0],
        [0,1,1,1],
        [1,0,0,1],
        [1,0,1,0],
        [1,0,1,1],
        [1,1,0,0],
        [1,1,0,1],
        [1,1,1,0],
        [1,1,1,1]
    ])
    G = np.concatenate((P,I),axis=1)
    c=np.dot(s,G)%2
    return c
s = [1,1,1,0,1,0,0,0,1,1,1]
print("Słowo wejściowe:", s)
print("Słowo zakodowane",hamming1511(s))0

def dechamming1511(c): #nie dziala poprawnie
    I = np.eye(4)
    P = np.array([
        [0,0,1,1],
        [0,1,0,1],
        [0,1,1,0],
        [0,1,1,1],
        [1,0,0,1],
        [1,0,1,0],
        [1,0,1,1],
        [1,1,0,0],
        [1,1,0,1],
        [1,1,1,0],
        [1,1,1,1]
    ])
    PT = np.transpose(P)
    I = np.eye(4)
    H = np.concatenate((I,P.T),axis=1)
    s = np.dot(c,H.T) % 2
    return s
c = hamming1511(s)
print(dechamming1511(c))