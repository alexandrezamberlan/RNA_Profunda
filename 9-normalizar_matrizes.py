def normalizarLinhasDeMatriz(matriz):
    """
    implementa o método que normaliza cada linha da matriz
    
    matriz -- uma matriz[n,m] estilo numpy
    
    matriz_normalizada -- matriz normalizada pela linha
    """
    
    #np.linalg.norm(..., ord = 2, axis = ..., keepdims = True)
    matriz_normalizada = np.linalg.norm(matriz,axis=1,keepdims=True)
    print ("matriz x normalizada: " + str(matriz_normalizada))
    # Divide matriz pela matriz_normalizada
    matriz = matriz / matriz_normalizada
    
    return matriz
    
x = np.array([
    [0, 3, 4],
    [1, 6, 4]])
print("Normalização da matriz x = " + str(normalizarLinhasDeMatriz(x)))    
