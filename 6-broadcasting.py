'''
                Maças   Carnes   Ovos   Batatas
carboidratos    56      0.0      4.4    68   
proteinas       1.2     104      52     8
gordura         1.8     135      99     0.9
'''

import numpy as np

a = np.array([[56, 0, 4.4, 68],
              [1.2, 104, 52, 8],
              [1.8, 135, 99, 0.9]])
print(a)              

calorias = a.sum(axis=0) #axis=0 significa coluna, enquanto axis=1 significa linhas
print("Calorias para cada alimento/coluna: " ,calorias)

#calculando a porcentagem de cada valor sobre a caloria total
porcentagem = 100*a/calorias.reshape(1,4)
print("A porcentagem para cada alimento")
print(porcentagem)

'''
Ideia geral de broadcasting é

matriz(m,n)   (+ ou - ou * ou /)   matriz(1,n)  -> matriz(m,n)
'''