fs = 22050
Tc = 1
N = Tc * fs
t=np.linspace(0,Tc,N)
b1=0
for h in range(1,3):
    b1+=(np.sin(6 * np.pi * t * (h ** 2)))/(((2 * h + 1) ** 2) + np.sin(12 * np.pi * t))
plt.plot(t, b1)
plt.show()
b2=0
for h in range(1,7):
    b2+=(np.sin(6 * np.pi * t * (h ** 2)))/(((2 * h + 1) ** 2) + np.sin(12 * np.pi * t))
plt.plot(t,b2)
plt.show()
b3=0
for h in range(1,27):
    b3+=(np.sin(6 * np.pi * t * (h ** 2)))/(((2 * h + 1) ** 2) + np.sin(12 * np.pi * t))
plt.plot(t, b3)
plt.show()