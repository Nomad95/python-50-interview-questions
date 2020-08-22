"""
Korzystając ze słownika stworzonego w poprzednim
zadaniu, sprawdź, czy któraś z liter wystąpiła w stringu
dokładnie 4 razy. Jeśli tak – wypisz True, jeśli nie – False.
"""

x = "myszydokazujągdykotanieczują"

D = dict()

for letter in list(x):
    get = D.setdefault(letter, 0)
    D[letter] = 1 + get

print(D)


####

wasExactly4Times = False

for value in D.values():
    if value is 4:
        wasExactly4Times = True


print(wasExactly4Times)