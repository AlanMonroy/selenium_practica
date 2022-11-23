import time
import numpy as np

#Opcion 1
start = time.time()
suma = int()
for i in range(100000000):
    suma += i

print(f"La suma es {suma}, con un tiempo de {time.time()-start}")

#Opcion 2
start = time.time()
suma2 = sum(range(100000000))
print(f"La suma es {suma2}, con un tiempo de {time.time()-start}")

#Opcion 3
start = time.time()
suma3 = np.sum(np.arange(100000000))
print(f"La suma es {suma3}, con un tiempo de {time.time()-start}")
