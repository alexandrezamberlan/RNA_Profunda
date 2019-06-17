#a função de custo de uma RNA profunda é baseada no Gradiente Descendente, que por sua vez se utiliza da derivada da sigmoide....

import numpy as np

def sigmoiide_derivada(x):
  s = 1 / (1 + np.exp(-x))
  ds = s * (1 - s)
  return ds

x = np.array([1, 2, 3])
print ("A derivada sigmóide de x = " + str(sigmoiide_derivada(x)))
