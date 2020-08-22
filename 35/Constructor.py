"""
Do czego w Pythonie służy __init__ ? Czym różni się od
__init__.py ?
Napisz fragment kodu wykorzystujący __init__.
"""


class Pies:

    def __init__(self, imie):
        a = 5
        b = 11
        self.imie = imie


psiax = Pies('Rudy')
psiax2 = Pies('Śukip')

print(psiax.imie)
print(psiax2.imie)

