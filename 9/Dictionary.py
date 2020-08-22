"""
Dla danego stringa x stwórz słownik przechowujący
informację, ile razy dana litera wystąpiła w stringu.
x = "myszydokazujągdykotanieczują"
"""

x = "myszydokazujągdykotanieczują"

D = dict()

for letter in list(x):
    get = D.setdefault(letter, 0)
    D[letter] = 1 + get

print(D)
