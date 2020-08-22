"""
Napisz funkcję sprawdzającą, czy podane słowo jest
palindromem.
Uruchom funkcję, aby sprawdzić, czy palindromami są
słowa "kajak" i "anakonda".
"""

a = "kajak"
b = "palindron"

# 1

print(a == a[::-1])
print(b == b[::-1])


def isPalindrone(string):
    for i in range(int(len(string) / 2)):
        if string[i] != string[len(string) - 1 - i]:
            return False

    return True


print(isPalindrone(a))
print(isPalindrone(b))
