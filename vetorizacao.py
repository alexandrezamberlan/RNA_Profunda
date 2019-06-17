import numpy as np
import time

a = np.array([1,2,3,4])
print(a)

a = np.random.rand(1000000)
b = np.random.rand(1000000)

inicio = time.time()
c = np.dot(a,b)
fim = time.time()

print("Soluçao vetorizada: " + str(1000*(fim - inicio)) + " ms")
