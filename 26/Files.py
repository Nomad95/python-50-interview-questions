"""
Stwórz plik o nazwie "moj_plik.txt".
Wpisz do niego liczby od 1 do 100, każdą w nowej linijce.
Otwórz plik i zapisz jego zawartość do listy z_pliku.
"""


with open('moj_plik.txt', 'w') as file:
    for x in range(1,101):
        file.write(str(x) + '\n')

with open('moj_plik.txt', 'r') as file:
    lista = file.read().splitlines()
    print(lista)

