"""
Wyjaśnij, jak działa poniższa funkcja. Wyjaśnij, skąd
wzięły się wyniki zwrócone przez poszczególne
wywołania funkcji.
def dodaj_do_listy(n, lista=[]):
lista.append(n)
print(lista)

dodaj_do_listy(1)
dodaj_do_listy(2,[4,5])
dodaj_do_listy(3)
"""


def dodaj_do_listy(n, lista=[]):
    # argument domyslny powstaje raz wiec za kazdym wywolaniem funkcji do listy dopisywana jest kolejna wartosc
    # ale chyba w najnowszym pythonie to zmienili
    # clue -> nie uzywamy mutable objects w argumentach
    lista.append(n)
    print(lista)


dodaj_do_listy(1)
dodaj_do_listy(2, [4, 5])
dodaj_do_listy(3)
