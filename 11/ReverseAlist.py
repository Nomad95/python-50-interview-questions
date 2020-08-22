"""
Na podstawie listy jezyki stwórz listę jezyki_odwrocone
zawierającą elementy listy jezyki w odwróconej
kolejności.
"""

jezyki = ['Python', 'Java', 'C', 'Ruby']

# 1

jezyki.reverse()

print(jezyki)

jezyki.reverse()

# 2

print(jezyki[::-1])

# 3

print(list(reversed(jezyki)))

