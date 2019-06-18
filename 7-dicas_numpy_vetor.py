import numpy as np

a = np.random.rand(5) #aqui, temos um vetor
print(a)
print("A dimensao da matriz é: ", a.shape) #mas não fica explicito que é de uma linha

print("Transposta de a")
print(a.T)

print("--------------Explicitando linha e coluna de matriz-------------------")

#portanto, melhor é criar um vetor de 5 linhas e 1 coluna
a = np.random.randn(5,1)
print(a)
print("A dimensao da matriz é: ", a.shape)

#agora tem sentido a transposta de a, ou seja, antes seria vetor de 5 linhas e 1 coluna
#a transposta vira um vetor de 1 linha e 5 colunas
print("Transposta de a")
print(a.T)

#agora também faz sentido a multiplicação de a por transposta de a

c = np.dot(a,a.T)
print("Matriz resultado da multiplicação de a pela sua transposta")
print(c)

