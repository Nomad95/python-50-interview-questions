"""
Do czego służą dekoratory @staticmethod i
@classmethod?
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

