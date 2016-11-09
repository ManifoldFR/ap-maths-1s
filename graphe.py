import numpy as np
import matplotlib
import matplotlib.pyplot as plt

def F(t):
    a = t*t - t - 12
    return (-12/a,4*t/a)

bounds = [[-4,-3.1],[-2.8,3.8],[4.1,5]]
opt = ['-','--','-.']

fig = plt.figure()
ax = fig.add_subplot(111)

for i, b in enumerate(bounds):
    T = np.linspace(*b,300)
    X,Y = F(T)
    lbl = r'$t\in[{0}, {1}]$'.format(b[0],b[1])
    ax.plot(X,Y, opt[i],
           label=lbl
           )

ax.legend()
ax.grid()
fig.show()