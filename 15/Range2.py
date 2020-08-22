"""
Napisz funkcję, która sprawdzi, czy podany string
zaczyna się słowem "python" i kończy rozszerzeniem
".py".
Przetestuj nią stringi:
"""

a = "python_moj_kod.py"
b = "python_notatki.txt"


def is_py(s):
    if s[0:6] == "python" and s[-3:] == ".py":
        return True

    return False

print(is_py(a))
print(is_py(b))