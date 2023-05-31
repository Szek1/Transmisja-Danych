import numpy as np
import matplotlib.pyplot as plt
x=np.arange(0,100,1)
y=np.cos(x)
plt.plot(x,y)
plt.savefig("xy.png")
plt.show()
