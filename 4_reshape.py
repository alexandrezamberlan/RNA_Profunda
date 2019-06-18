# duas funções importantes no pacote numpy para deep learning são np.shape() e np.reshape()
# x.shape é utilizada para descobrir o shape (dimensão) da matriz/vetor x
# x.reshape(...) é usado para remodelar x em outra dimensão

'''
Na Ciência da Computação, por exemplo, uma imagem é uma matriz 3D de shape (length,height,depth=3)(length,height,depth=3). 
Porém, quando uma imagem é lida como entrada de um algoritmo, é necessário converter a imagem para um vetor de 
shape (length∗height∗3,1)(length∗height∗3,1)

Essa expressão é 'desenrolar' ou redesenhar/remodelar (reshape) a matriz 3D em um vetor 1D.
'''
import numpy as np
a = np.random.randn(3,3)
b = np.random.randn(3,1)

print(a.shape)
print(b.shape)

c = a * b
print(c.shape)
