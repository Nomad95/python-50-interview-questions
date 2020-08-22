"""
Wypisz podaną listę imion, przed każdym dodając
kolejny numer. Zacznij numerowanie od 1.
"""

imiona = ['Adam', 'Stanisław', 'Maria', 'Zofia',
'Mikołaj']

for count, name in enumerate(imiona, 1):
    print(count, name)