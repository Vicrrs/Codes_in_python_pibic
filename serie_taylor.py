import numpy as np
import matplotlib.pyplot as plt


def taylor(der,x,xo,N):
  soma = 0.0
  potencia = 1
  factorial=1
  for i in range(N):
      soma = soma + der[i]*potencia/factorial
      potencia = potencia*(x-xo)
      factorial = factorial*(i+1)

  return soma 


numero_pontos=100

X = np.linspace(-4,4,numero_pontos)

# Y é um vetor cujas componentes são os senos de cada valor do vetor X 
# A função seno pode ser moficiada por outra função da libraria numpy
Y = np.sin(X)

plt.plot(X,Y)
plt.xlabel('x')
plt.ylabel('y')
plt.axvline(x=0,color='k')
plt.axhline(y=0,color='k')

N = 6
Y1 = []
# der é um vetor que contem as derivadas avaliadas em xo
der = np.array([0,1,0,-1,0,1])
for j in range(numero_pontos):
    Y1.append(taylor(der,X[j],0.0,N))

plt.plot(X,Y1)
plt.show()