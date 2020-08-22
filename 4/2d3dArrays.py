"""
Jakiej struktury danych użyłbyś do zamodelowania
szafki, która ma 3 szuflady, a w każdej z nich znajdują się
3 przegródki?
Stwórz taki model i umieść stringa "długopis" w
środkowej przegródce środkowej szuflady.
"""

T = [[[""] for x in range(3)] for x in range(3)]

T[1][1][0] = "Długopis"

print(T)

for x in T:
    print(x)


