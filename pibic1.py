import numpy as np
import matplotlib.pyplot as plt

a = 1.0

t = 1.0

epsilon_0 = 2.0

N = 80

nu = np.linspace(-N/2, N/2, N)

k = (2*np.pi/(N*a))*nu

E = epsilon_0 -2*t*np.cos(k*a)

plt.plot(k, E, 'o-')

plt.xlabel('k', fontsize = 18)
plt.ylabel('E', fontsize = 18)

plt.show()