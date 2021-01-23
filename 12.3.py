import random
import math


def mediana_sort(L):
    K = []
    for i in range(len(L)):
        K.append(L[i])

    K.sort()

    rightK = len(K) - 1
    mid = (rightK) / 2
    if len(K) % 2:
        return K[math.floor(mid)]
    else:
        return (K[math.floor(mid)] + K[math.floor(mid) + 1]) / 2


n = 20
k = 10
L = []

for i in range(n):
    L.append(random.randint(0, k-1))

print("Mediana :")
print(str(mediana_sort(L)))
