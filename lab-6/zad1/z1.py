import numpy as np

def koder74(s):
    x1 =(s[0] + s[1] + s[3]) %2
    x2 = (s[0] + s[2] + s[3]) %2
    x4 = (s[1] + s[2] + s[3]) %2
    out  = [x1, x2 , s[0] , x4 , s[1] , s[2],s[3]]
    return out

slowo = [1,1,0,1]
koder = koder74(slowo)
print("Słowo wejściowe: " + str(slowo))
print("Słowo zakodowane: " + str(koder))

def dekoder74(s):
    x1 = (s[0] + s[2] + s[4] + s[6]) %2
    x2 = (s[1] + s[2] + s[5] + s[6]) %2
    x4 = (s[3] + s[4] + s[5] + s[6]) %2
    S = (x1 * np.power(2,0)) + (x2 * np.power(2,1)) + (x4 * np.power(2,2))
    print(S)
    if S == 0:
        return [s[2],s[4],s[5],s[6]]
    elif S != 0:
        b = S-1
        if s[b] == 0:
            s[b] = 1
        else:
            s[b] = 0
    return [s[2], s[4], s[5], s[6]]



koder = koder74(slowo)
dekoder = dekoder74(koder)

print("Słowo odkodowane: "+ str(dekoder))
