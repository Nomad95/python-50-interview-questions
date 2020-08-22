"""
Napisz funkcję, która dla podanego katalogu wypisze
znajdujące się w nim pliki.
Pamiętaj, że katalog może zawierać podkatalogi, do
których funkcja również musi zajrzeć.
"""
import os



def search(root):
    for dir in os.listdir(root):
        fullPath = os.path.join(root, dir)
        if os.path.isdir(fullPath):
            search(fullPath)
        else:
            print(fullPath)


search(".")