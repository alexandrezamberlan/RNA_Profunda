def L1(yhat, y):
    """
    Arguments:
    yhat -- a expectativa de y de tamanho m (predicted labels)
    y -- vetor de tamanho m (true labels)
    
    Returns:
    perda -- np.sum(abs(yhat - y))
    """
    perda = np.sum(abs(yhat - y))
    
    return perda


def L2(yhat, y):
    return np.sum(np.dot(y - yhat, y - yhat))    
    
    
#expectativa da saída em y
yhat = np.array([.9, 0.2, 0.1, .4, .9])

#realidade de saída em y
y = np.array([1, 0, 0, 1, 1])

#cálculo da perda L1
print("L1 = " + str(L1(yhat,y)))    


#cálculo da perda L2
print("L1 = " + str(L2(yhat,y)))  
