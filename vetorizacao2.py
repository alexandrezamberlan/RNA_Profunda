#imagine que seja preciso aplicar o exponencial para cada elemento de uma matriz/vetor

#v = [v1, ..., vn] -> u = [exp(v1), exp(v2), ..., exp(vn)]

#solução não vetorizada seria
import numpy as np
import time

u = np.zeros((n,1))
for i in range(n):
  u[i] = math.exp(v[i])
