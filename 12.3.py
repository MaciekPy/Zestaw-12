import random


def mediana_sort(L, left, right):

    L.sort()
    mid = (len(L) // 2)
    if len(L) % 2:
        return L[mid]
    else:
        return (L[mid] + L[mid + 1]) / 2


n = 100
k = 10
L = []

for i in range(n):
    L.append(random.randint(0, k-1))

print("Mediana :")
print(str(mediana_sort(L, 0, n-1)))
