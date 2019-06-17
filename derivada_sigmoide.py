import numpy as np

def sigmide_derivada(x):
  s = 1 / (1 + np.exp(-x))
