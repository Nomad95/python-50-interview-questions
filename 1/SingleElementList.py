"""
Korzystając z podanej listy A, stwórz listę B, która będzie
zawierać tylko unikalne elementy z listy A.
A = [1,2,3,3,2,1,2,3]
"""

A = [1,2,3,3,2,1,2,3]

# 1

B = list(set(A))
print(B)

# 2

B2 = []

for el in A:
    if not B2.__contains__(el):
        B2.append(el)

print(B2)