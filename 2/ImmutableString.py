"""
Modyfikacja stringa

Co się stanie po wykonaniu poniższego kodu?
a = ‘abcdefg’
a[1] = ‘X’
"""

a = 'abcdefg'

# 1

split = list(a)
print(split)
split[1] = 'X'
a = "".join(split)

print(a)
