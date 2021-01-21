import random


def linear_search(L, left, right, y):
    indexes = []
    i = left
    while i <= right:

        if y == L[i]:
            indexes.append(i)
        i += 1
    return indexes


n = 100
k = 10
L = []

for i in range(n):
    L.append(random.randint(0, k-1))

y = random.randint(0, k-1)
print("wylosowana liczba : " + str(y))
print("znalezione indexy :")
print(str(linear_search(L, 0, n-1, y)))
