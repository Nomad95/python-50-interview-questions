"""
Do czego w Pythonie służy słowo kluczowe yield ?
Napisz przykładowy kod wykorzystujący yield.
"""


def generate10():
    for i in range(1, 11):
        yield i


gen = generate10()

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
