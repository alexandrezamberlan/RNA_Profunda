'''
Para redimensionar matrizes, há basicamente 2 funções usadas em deeplearning: np.shape() and np.reshape().

    matriz.shape é utilizada para descobrir a dimensão da matriz/vetor
    matriz.reshape(...) é usada para redimensionar matriz em outro tamanho/dimensão

Uma imagem é um vetor 3D de dimensão (length,height,depth=3)(length,height,depth=3).

Porém, esta imagem precisa ser desenrolada em vetor de dimensões (length∗height∗3,1)(length∗height∗3,1). 
'''

# imagine uma matriz[3,2,3], em que o último 3 representa a dimensão para valores RGB
imagem = np.array([[[ 0.67826139,  0.29380381],
        [ 0.90714982,  0.52835647],
        [ 0.4215251 ,  0.45017551]],

       [[ 0.92814219,  0.96677647],
        [ 0.85304703,  0.52351845],
        [ 0.19981397,  0.27417313]],

       [[ 0.60659855,  0.00533165],
        [ 0.10820313,  0.49978937],
        [ 0.34144279,  0.94630077]]])

print ("Quantidade de elementos: " + imagem.shape[0] * imagem.shape[1] * imagem.shape[2])

vetor_da_imagem = imagem.reshape(imagem.shape[0] * imagem.shape[1] * imagem.shape[2])

print ("Vetor com os dados da matriz desenrolada: " + str(vetor_da_imagem))
