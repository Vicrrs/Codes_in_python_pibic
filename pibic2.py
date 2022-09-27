import numpy as np
import matplotlib.pyplot as plt

a = 1.0 

t = 1.0

epsilon_0 = 0.0
epsilon_AB = 2.0

N = 80

nu = np.linspace(-N/2,N/2,N)

k = (2*np.pi/(N*a))*nu

A = np.sqrt(epsilon_AB*epsilon_AB+t*t-2*t*epsilon_AB*np.cos(k*a))

E1 = epsilon_0 - A

E2 = epsilon_0 + A

plt.plot(k,E1,'o-')
plt.plot(k,E2,'o-')

plt.xlabel('k', fontsize = 18)
plt.ylabel('E', fontsize = 18)

plt.show()
