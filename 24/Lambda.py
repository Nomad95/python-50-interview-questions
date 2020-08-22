"""
Uzyj lambdy
"""

# Sortuje po 2gim  elemencie tupli
second_tupel = lambda x: x[1]

L = [(1, 5), (4, 2), (6, 4)]

L.sort(key=second_tupel)

print(L)


A = [1,2,3,4,5]
B = A
C = A[:]
C = list(A)
A[0] = 111

print(A, B, C)

