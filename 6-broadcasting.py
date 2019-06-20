'''

Um conceito muito importante para entender no pacote numpy é "broadcasting". 
É muito útil para executar operações matemáticas entre arrays de diferentes dimensões.
Veja http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html

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

print("Outro exemplo de broadcasting.....")
def softmax(x):
    """Calcula softmax para cada linha de x.

    Funciona em vetor e matrizes[n, m].

    Argument:
    x -- matriz do pacote numpy de dimensão (n,m)

    Returns:
    resultado -- matriz numpy igual ao softmax de x (n,m)
    """
    
    x_elevada = np.exp(x)  

    x_somada = np.sum(x_elevada, axis = 1, keepdims = True)
    
    resultado = x_elevada / x_somada
    
    return resultado
  
matriz = np.array([
    [9, 2, 5, 0, 0],
    [7, 5, 0, 0 ,0]])

print("softmax da matriz = " + str(softmax(matriz)))  
