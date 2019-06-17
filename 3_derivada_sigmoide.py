# a função de custo (média de todas as perdas) de uma RNA profunda é baseada no Gradiente Descendente, que por sua vez se utiliza da derivada da sigmoide....
# os gradientes são usados para otimizar as funções de perda usando a retropropagação

import numpy as np

def sigmoide_derivada(x):
  s = 1 / (1 + np.exp(-x))
  ds = s * (1 - s)
  return ds

x = np.array([1, 2, 3])
print ("A derivada sigmóide de x = " + str(sigmoide_derivada(x)))
 