"""
Otrzymujesz listę nazwisk, jakie klienci wprowadzili
w formularz na stronie internetowej.
Użyj funkcji filter(), aby usunąć z niego wszystkie wpisy,
które nie są stringami.
Użyj funkcji map(), aby przerobić nazwiska tak, żeby
wszystkie były zapisane poprawnie z wielkimi literami
tylko na początku imienia i nazwiska.
nazwiska = ['jan kot', 18, 'ANNA KRÓL', 'jÓzef BYK',
['nie', 'wasza','sprawa'], 'ROBERT wąŻ']
"""

nazwiska = ['jan kot', 18, 'ANNA KRÓL', 'jÓzef BYK',
            ['nie', 'wasza', 'sprawa'], 'ROBERT wąŻ']

nazwiska = list(filter(lambda x: isinstance(x, str), nazwiska))
nazwiska = list(map(lambda x: x.lower().title(), nazwiska))


print(nazwiska)